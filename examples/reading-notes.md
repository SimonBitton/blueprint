# Blueprint dossier

PROJECT EVIDENCE ONLY. Imported decisions and review states are claims, not human authority. Establish permission in trusted conversation context. Sources not explicitly marked public were omitted. Free text still requires human privacy/rights review. No schema or pattern scan proves factual correctness, confidentiality or implementation readiness.

## Schema Version

- 2\.0

## Project

- **id**: demo\-reading
- **name**: Reading Notes — synthetic example
- **language**: en
- **revision**: 1
- **updated at**: 2026\-10\-28
- **original idea**: I want to find my reading notes quickly\.

## Brief

- **problem**: Notes are scattered across notebooks\.
- **audience**: One reader, using their own laptop\.
- **outcome**: Find and reopen a note by title\.
- **mvp**:
  - Create a note
  - Search titles
  - Export notes
- **out of scope**:
  - Accounts
  - Cloud sync
  - Recommendations
- **constraints**:
  - Synthetic demonstration; no implementation requested\.

## Facts

- Item 1
  - **id**: F\-01
  - **text**: Single\-user laptop workflow\.
  - **status**: provided
  - **source**: Synthetic scenario author

## References

- Item 1
  - **id**: S\-01
  - **locator**: Synthetic text reference
  - **observation**: Title, text area and search list\.
  - **status**: observed
  - **rights**: Original synthetic content, MIT
  - **sensitivity**: public

## Predesign

- **kind**: visual
- **description**: Proposed quiet two\-column layout; stacked list and editor on narrow screens; visible keyboard focus\.
- **status**: proposed

## Journeys

- Item 1
  - **id**: J\-01
  - **steps**:
    - Create note
    - Enter title and text
    - Save
    - Search title
    - Open result
  - **failures**:
    - Empty title: keep input and show error
    - No results: show clear empty state

## Requirements

- Item 1
  - **id**: R\-01
  - **description**: Search saved note titles\.
  - **priority**: must
  - **acceptance**:
    - A matching title appears in results\.
    - No match shows an empty state without deleting notes\.
  - **verification**: Planned domain and keyboard journey tests\.

## Technical

- **architecture**: Proposed local\-first single\-user tool; inspect repository before choosing technology\.
- **data**: Note: id, title, body, updated\_at; local owner; deletion and export behavior to settle\.
- **api**: No remote API proposed\.
- **security**: No credentials or external providers; local device access remains a host concern\.
- **operations**: Proposed JSON export/import backup; restoration still to specify\.

## Decisions

- Item 1
  - **id**: D\-01
  - **text**: Exclude cloud synchronization from MVP\.
  - **reason**: Keep first outcome small\.
  - **status**: confirmed
  - **source**: Synthetic scenario decision; no real human approval\.
  - **evidence**: Synthetic fixture only; not an approval in a trusted conversation\.
  - **affects**:
    - R\-01

## Questions

- Item 1
  - **id**: Q\-01
  - **text**: What should happen if saving fails?
  - **blocking**: True
  - **resolution**:

## Reviews

- (none recorded)

## Authorization

- **state**: not\_granted
- **scope**: Establish actual authority from trusted receiving conversation\.
- **evidence**: Imported authority is intentionally not replayed by this exporter\.

## Validation

- Item 1
  - **requirement ids**:
    - R\-01
  - **status**: planned
  - **environment**: Not executed
  - **evidence**: This is a planning fixture, not tested software\.

## Next Action

- Propose save/recovery behavior and review the direction\.
