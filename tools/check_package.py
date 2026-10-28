#!/usr/bin/env python3
"""Check skill format, bundled references and accidental publication hazards."""
import json
from pathlib import Path
import re
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/blueprint'


def check(root=ROOT):
    skill = root / 'skills/blueprint'
    raw = (skill/'SKILL.md').read_text(encoding='utf-8')
    assert raw.startswith('---\n'), 'Missing frontmatter'
    head, body = raw[4:].split('\n---\n', 1)
    meta = yaml.safe_load(head)
    assert set(meta) <= {'name','description','license','compatibility','metadata','allowed-tools'}
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', meta['name'])
    assert meta['name'] == skill.name and len(meta['name']) <= 64
    assert 1 <= len(meta['description']) <= 1024
    assert meta['license'] == 'MIT'
    assert all(isinstance(k,str) and isinstance(v,str) for k,v in meta['metadata'].items())
    assert meta['metadata']['version'] == (root/'VERSION').read_text().strip() == (skill/'VERSION').read_text().strip()
    assert len(body.splitlines()) < 500
    ui = yaml.safe_load((skill/'agents/openai.yaml').read_text())
    assert '$blueprint' in ui['interface']['default_prompt']
    assert 25 <= len(ui['interface']['short_description']) <= 64
    assert ui.get('policy',{}).get('allow_implicit_invocation',True)
    for path in root.rglob('*'):
        if '.git' in path.parts or '__pycache__' in path.parts:
            continue
        assert not path.is_symlink(), 'Symlinks not allowed in release'
        if not path.is_file():
            continue
        assert path.name not in {'.DS_Store','.env','.env.local','id_rsa','id_ed25519'}, 'Private file in release'
        assert 'node_modules' not in path.parts and '.venv' not in path.parts
        if path.suffix in {'.md','.yaml','.json','.py','.txt'}:
            text = path.read_text(encoding='utf-8')
            assert not re.search(r'/(?:Users|home)/', text), 'Private absolute path in release'
            assert not re.search(r'\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bsk-[A-Za-z0-9_-]{30,}\b',text), 'Possible secret'
            if path.suffix == '.md':
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                    if '://' not in target and not target.startswith(('#','mailto:')):
                        target_path = target.split('#')[0]
                        if target_path:
                            resolved = (path.parent/target_path).resolve()
                            assert resolved.is_relative_to(root.resolve()), 'Reference escapes repository'
                            assert resolved.exists(), f'Broken relative link in {path.relative_to(root)}: {target}'
    schema = json.loads((skill/'assets/project.schema.json').read_text())
    Draft202012Validator.check_schema(schema)
    assert (skill/'LICENSE').read_bytes() == (root/'LICENSE').read_bytes()
    print('PASS: format, metadata, versions, references, schema, package paths and basic secret scan.')


if __name__ == '__main__':
    try:
        check()
    except (AssertionError, ValueError, KeyError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr)
        sys.exit(1)
