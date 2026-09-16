# Project Memory

This is the living state file for the University Timetable Management System. AI coding agents must read it before substantial work and update it after meaningful progress.

## Project Status
Documentation V2 completed from review of the supplied university timetable.

## Current Phase
Phase 0 - Documentation and Repository

## Current Task
Prepare repository and development environment before application implementation.

## Completed
- Product concept defined.
- Student, teacher and admin roles defined.
- Modular Django architecture defined.
- Six project-control documents created.
- Supplied timetable reviewed.
- Real variable-duration timetable behavior recognized.
- Versioning, conflicts, history, effective dates, overrides, cancellations, rescheduling, substitutions, approval/publication and notifications defined.

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
Repository initialization and Codex-ready project setup.

## Next Tasks
1. Create GitHub repository.
2. Add the V2 documentation files.
3. Configure Codespaces/development environment.
4. Initialize Django.
5. Verify development server.
6. Update memory.md.
7. Begin Phase 1 only after foundation is working.

## Do Not Implement Yet
Automatic scheduling, complex optimization, native mobile app, microservices, external notification infrastructure and advanced AI scheduling.

## Known Unknowns
Official university branding; exact academic hierarchy; student/teacher identifiers; room capacity/capability rules; academic session dates; approval authority; notification channels; campus structure; existing SIS/LMS integration; import format; special/Saturday rules; conflict-waiver authority.

## AI Boundaries
AI must not invent university policy, decide whether a real conflict is acceptable, overwrite history, publish without authorization, or claim completion without verification.

## Change Log
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
V2 - after review of supplied university timetable.
