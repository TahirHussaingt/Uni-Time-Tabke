# Rules - University Timetable Management System

## Core Rules
1. Treat timetable data as versioned, changeable and auditable.
2. Never destructively overwrite important published history.
3. The current effective published version is the official source for students and teachers.
4. Draft/tentative/review data must remain clearly separated from published data.
5. Store actual start and end times.

## Conflict Rules
Always check teacher overlap, room overlap, section overlap, time overlap, capacity, room/lab compatibility and duplicate active entries.

A conflict may be blocked, corrected, kept in draft, or explicitly waived by an authorized human with a recorded reason. AI must not decide that a real university conflict is acceptable.

## Change Rules
Published modifications must preserve old/new values, who changed them, when, why and when they become effective.

Cancellation is a state/change, not deletion.

Rescheduling preserves the original schedule history and creates the new effective schedule.

Temporary teacher replacement must be represented explicitly and must not silently erase the permanent assignment.

## Effective Dates
Support one-day changes, date ranges and permanent changes from an effective date.

## Publication
Do not automatically publish imports, generated schedules, drafts or unresolved conflict sets. Use explicit authorization.

## Libraries
Prefer Python/Django standard functionality. Add packages only for a documented need, and keep dependencies minimal and maintained. Do not add popular libraries merely because they are popular.

Initial environment should remain small: Django, PostgreSQL driver when needed, selected testing tools, and later PDF/Excel libraries only when those features are implemented.

## Error Handling
Expected validation errors must be clear and actionable. Unexpected errors must be logged and shown safely. Avoid empty `except` blocks, catch-all handling everywhere, silent failures and production stack traces.

Use database transactions for publication, complex revisions, multi-record imports and other atomic operations.

## Security
Never hard-code secrets or commit `.env` credentials. Enforce server-side permissions, validate input, use CSRF protection, protect personal data and never log passwords/tokens.

## AI / Codex Boundaries
Before substantial implementation, AI must read all six project-control documents.

AI must inspect current code, make focused changes, preserve working behavior, respect architecture, run relevant checks, update `memory.md` and identify assumptions.

AI must not rebuild the project without instruction, add arbitrary dependencies, silently redesign the database, erase timetable history, publish schedules without authorization, invent university policy/data, or claim completion without verification.

## Git
Use small meaningful commits such as:
- `docs: update timetable requirements`
- `feat: add timetable version model`
- `feat: add conflict detection`
- `fix: prevent room overlap`
- `feat: add revision history`

Do not commit credentials or sensitive production data.
