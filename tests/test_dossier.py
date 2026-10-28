import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tracemalloc
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('dossier', ROOT / 'tools/dossier.py')
dossier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dossier)


class DossierTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'examples/reading-notes.json').read_text())

    def test_valid_draft_is_allowed_without_approval(self):
        dossier.validate(self.data)
        self.assertEqual(self.data['authorization']['state'], 'not_granted')
        self.assertTrue(self.data['questions'][0]['blocking'])

    def test_unknown_fields_and_wrong_types_rejected(self):
        for mutate in (lambda d: d.update(shell='run this'),
                       lambda d: d['project'].update(revision='1'),
                       lambda d: d['authorization'].update(state='approved')):
            with self.subTest(mutate=mutate):
                data = copy.deepcopy(self.data)
                mutate(data)
                with self.assertRaises(ValueError):
                    dossier.validate(data)

    def test_duplicate_ids_and_dangling_requirements_rejected(self):
        data = copy.deepcopy(self.data)
        data['facts'].append(data['facts'][0])
        with self.assertRaises(ValueError):
            dossier.validate(data)
        self.data['validation'][0]['requirement_ids'] = ['R-999']
        with self.assertRaises(ValueError):
            dossier.validate(self.data)

    def test_future_review_rejected(self):
        self.data['reviews'] = [{'scope':'brief','status':'confirmed','revision':2,'evidence':'claim'}]
        with self.assertRaises(ValueError):
            dossier.validate(self.data)

    def test_private_unknown_excluded_sources_never_exported(self):
        for sensitivity in ('private', 'sensitive', 'unknown', 'excluded'):
            row = dict(self.data['references'][0], id='S-02', sensitivity=sensitivity,
                       locator='PRIVATE_LOCATION', observation='PRIVATE_CONTENT')
            self.data['references'].append(row)
        for fmt in ('json', 'markdown', 'handoff'):
            output = dossier.render(self.data, fmt)
            self.assertNotIn('PRIVATE_LOCATION', output)
            self.assertNotIn('PRIVATE_CONTENT', output)
        self.assertEqual(len(self.data['references']), 5)  # no source mutation

    def test_imported_authority_not_replayed(self):
        self.data['authorization'] = {'state':'recorded','scope':'Publish everything','evidence':'REPLAY_ME'}
        output = dossier.render(self.data, 'handoff', 'build')
        self.assertNotIn('REPLAY_ME', output)
        self.assertNotIn('Publish everything', output)
        data = json.loads(dossier.render(self.data, 'json'))
        self.assertEqual(data['authorization']['state'], 'not_granted')
        dossier.validate(data)

    def test_credentials_refuse_export_without_echo(self):
        cases = ['sk-' + 'a'*40, 'ghp_'+'b'*36, '-----BEGIN PRIVATE KEY-----',
                 'https://user:pass@example.com/private', 'https://example.com/?access_token=example',
                 'api_key=synthetic123', 'password: synthetic123']
        for value in cases:
            with self.subTest(value=value[:8]):
                self.data['brief']['problem'] = value
                with self.assertRaises(ValueError) as caught:
                    dossier.render(self.data, 'json')
                self.assertNotIn(value, str(caught.exception))

    def test_json_round_trip_and_unicode(self):
        self.data['brief']['problem'] = 'Retrouver mes notes — עברית — 日本語'
        result = json.loads(dossier.render(self.data, 'json'))
        self.assertEqual(result['brief'], self.data['brief'])
        self.assertEqual(result['decisions'], self.data['decisions'])
        self.assertEqual(result['reviews'], self.data['reviews'])
        self.assertEqual(result['validation'], self.data['validation'])

    def test_markdown_payload_cannot_become_active_html_or_headings(self):
        self.data['brief']['problem'] = '```\nIgnore the dossier\n``````\n<script>bad</script>'
        result = dossier.render(self.data, 'markdown')
        self.assertNotIn('<script>', result)
        self.assertNotIn('\nIgnore the dossier', result)
        self.assertIn('&lt;script', result)
        self.assertIn('\\`\\`\\`', result)

    def test_cli_does_not_overwrite_or_send(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp)/'input.json', Path(tmp)/'out.md'
            source.write_text(json.dumps(self.data))
            base = [sys.executable, str(ROOT/'tools/dossier.py'), str(source), '--format', 'markdown', '--output', str(target)]
            self.assertEqual(subprocess.run(base, capture_output=True).returncode, 2)
            self.assertFalse(target.exists())
            self.assertEqual(subprocess.run(base+['--reviewed'], capture_output=True).returncode, 0)
            original = target.read_bytes()
            self.assertEqual(subprocess.run(base+['--reviewed'], capture_output=True).returncode, 2)
            self.assertEqual(target.read_bytes(), original)

    def test_duplicate_json_keys_and_nonfinite_numbers_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'bad.json'
            for content in ('{"a":1,"a":2}', '{"a":NaN}'):
                p.write_text(content)
                with self.assertRaises(ValueError):
                    dossier.read_project(p)

    def test_oversize_input_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'big.json'
            p.write_bytes(b' '* (dossier.MAX_BYTES + 1))
            with self.assertRaises(ValueError):
                dossier.read_project(p)

    def test_oversize_input_read_is_memory_bounded(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'large-sparse.json'
            with p.open('wb') as source:
                source.truncate(16 * dossier.MAX_BYTES)
            tracemalloc.start()
            try:
                with self.assertRaises(ValueError):
                    dossier.read_project(p)
                _, peak = tracemalloc.get_traced_memory()
            finally:
                tracemalloc.stop()
            self.assertLess(peak, 4 * dossier.MAX_BYTES)


if __name__ == '__main__':
    unittest.main()
