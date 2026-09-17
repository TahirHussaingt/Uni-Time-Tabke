# Project Memory

This is the living state file for the University Timetable Management System. AI coding agents must read it before substantial work and update it after meaningful progress.

## Project Status
Phase 0 Django foundation initialized and verified locally.

## Current Phase
Phase 0 - Documentation and Repository

## Current Task
Phase 0 foundation completed; awaiting authorization to begin Phase 1.

## Completed
- Product concept defined.
- Student, teacher and admin roles defined.
- Modular Django architecture defined.
- Six project-control documents created.
- Supplied timetable reviewed.
- Real variable-duration timetable behavior recognized.
- Versioning, conflicts, history, effective dates, overrides, cancellations, rescheduling, substitutions, approval/publication and notifications defined.
- Django project configuration initialized (`config` package and `manage.py`).
- Development SQLite database initialized with Django's built-in migrations.
- Django system check, ASGI/WSGI imports and development server verified.

## Supplied Timetable Findings
The source is a tentative Computer Science BS-CS Fall-26 Morning timetable, uses Monday-Saturday and covers multiple BS-CS sections. It has display rows such as 8:30, 9:45, 11:00, 12:15, 1:30, 2:45 and 4:00, but also explicit intervals such as 8:30-10:10, 10:10-11:50, 11:50-1:30 and 3:10-4:50. Therefore actual start/end times are required in the data model.

## Major Product Decision
The timetable is not static. The application must support Draft -> Tentative -> Under Review -> Approved -> Published -> Superseded -> Archived.

## Versioning Decision
Never destructively overwrite published timetable history. Revisions must remain traceable.

## Change Requirements
Record affected item, old value, new value, reason, changed by, changed at, effective date and approval/publication status where relevant.

## Exception Requirements
Support one-day and date-range overrides for room, teacher, time, day, cancellation and replacement classes.

## Conflict Requirements
At minimum: teacher overlap, room overlap, section overlap, time overlap, room capacity, room/lab compatibility and duplicate active entries.

Conflict states: Open, Acknowledged, Resolved, Waived. Waiver requires authorized human action and a reason.

## Technology
Python, Django, SQLite for development, PostgreSQL for production, HTML/CSS/JavaScript, Git/GitHub and GitHub Codespaces or equivalent.

## Current Architecture Decision
Modular Django monolith. No microservices unless required.

## Current Authentication Decision
Use Django authentication/authorization unless a documented university requirement requires another solution.

## Currently Working On
No active implementation task.

## Next Tasks
1. Begin Phase 1 - Base UI, only when authorized.
2. Create the base template, branding placeholder, navigation, login layout,
   dashboard shell, responsive structure and error pages.

## Do Not Implement Yet
Automatic scheduling, complex optimization, native mobile app, microservices, external notification infrastructure and advanced AI scheduling.

## Known Unknowns
Official university branding; exact academic hierarchy; student/teacher identifiers; room capacity/capability rules; academic session dates; approval authority; notification channels; campus structure; existing SIS/LMS integration; import format; special/Saturday rules; conflict-waiver authority.

## AI Boundaries
AI must not invent university policy, decide whether a real conflict is acceptable, overwrite history, publish without authorization, or claim completion without verification.

## Change Log
### Phase 0 Django Foundation
- Added `manage.py` and the root `config` Django configuration package.
- Configured SQLite for local development and `Asia/Karachi` as the project time zone.
- Added `requirements.txt` pinned to the installed Django version (5.2.17).
- Added `.env.example`; a persistent `DJANGO_SECRET_KEY` is supplied through the environment outside isolated local development.
- Applied standard Django migrations to the ignored local SQLite database.
- Verified `manage.py check`, ASGI/WSGI imports and a local development-server request.

### V2 Documentation
- Reviewed supplied university timetable.
- Added real interval support.
- Added versioning/lifecycle states.
- Added conflict detection/resolution.
- Added change history.
- Added effective-date and temporary overrides.
- Added cancellation/rescheduling/substitution.
- Added approval/publication workflow.
- Added notifications.
- Updated dashboards, design and development phases.

## Last Updated
Phase 0 - Django foundation verified locally.
