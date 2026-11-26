# Create handoff entry

## Status

approved

## Intent

A teammate ending a focus block records who they are, how severe the note is, and a short summary. The service stores the note with a UTC timestamp and returns a stable id so later list and export tasks can find it.

## Requirements

- REQ-HANDOFF-CREATE-1 Store a handoff record with author id, UTC timestamp, severity, summary, and a stable id.
- REQ-HANDOFF-CREATE-2 Validate input before storage. Reject incomplete or illegal payloads without writing a partial row.

## Acceptance criteria

- AC-HANDOFF-CREATE-1 A valid payload is stored and the response includes a stable id.
- AC-HANDOFF-CREATE-2 Missing required fields return a clear client error and do not store a partial row.
- AC-HANDOFF-CREATE-3 Severity must be one of `info`, `warning`, or `critical`. Any other value is rejected and not stored.

## Contract

`POST /handoffs`

Required JSON fields:

- `author_id` — non-empty string, max 80 characters
- `severity` — `info`, `warning`, or `critical`
- `summary` — non-empty string, max 500 characters

The server sets `created_at` to the current UTC time. Success returns HTTP 201 with `id`, `author_id`, `created_at`, `severity`, and `summary`. Validation failures return HTTP 400 with an error message and do not insert a row.

## Out of scope

Accounts, authentication, and the list or export endpoints.

## Open questions

None.

## Amendments

2026-11-19 — Initial approved contract for the hackathon sprint.

Amended after implementation: note prefixes are display-only.
