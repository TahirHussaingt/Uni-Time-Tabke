# University Timetable Management System

## Project Overview
A centralized Django-based university timetable system for students, teachers, and administrators. The system must treat timetables as **tentative, versioned, changeable, conflict-prone, and auditable**, rather than as one permanent weekly grid.

## Real Timetable Findings
The supplied document is a tentative Computer Science BS-CS Fall-26 Morning timetable. It contains multiple sections, Monday-Saturday scheduling, visible rows such as 8:30 AM, 9:45 AM, 11:00 AM, 12:15 PM, 1:30 PM, 2:45 PM and 4:00 PM, plus explicit intervals such as 8:30-10:10 and 3:10-4:50. Therefore the database must store actual start/end times, not only row names. [Source: supplied timetable, PDF pp. 1-10.]

## Target Users
### Administrator / Timetable Coordinator
Manage academic data, students, teachers, courses, rooms, timetable drafts, conflicts, revisions, approvals, publication, cancellations, rescheduling, substitutions, notifications, reports, and imports/exports.

### Teacher
View official teaching timetable, today's/current/next classes, rooms, sections, changes, cancellations, substitutions, notifications, and report issues.

### Student
View official section timetable, today's/current/next classes, teacher/room information, changes, cancellations, tentative/published status, notifications, and report issues.

## Core Features
- Authentication and role-based permissions
- Departments, programs, sessions, semesters, sections
- Students and teachers
- Courses and course offerings
- Buildings and rooms
- Flexible start/end time intervals
- Draft/tentative/review/approved/published/superseded/archived versions
- Daily, weekly, student, teacher, section, room, course and department views
- Current/next class
- Teacher, room and section conflict detection
- Capacity and room/lab compatibility validation
- Timetable revisions and complete change history
- Effective dates and temporary overrides
- Room/teacher/time/day changes
- Cancellation and rescheduling
- Substitute teachers
- Notifications for affected users
- PDF/CSV/Excel/printable reporting
- CSV/Excel import with preview and validation
- Automatic scheduling only as a later, human-reviewed feature

## Timetable Lifecycle
Draft -> Tentative -> Under Review -> Approved -> Published/Active -> Superseded -> Archived

Class/session states may include Scheduled, Modified, Cancelled, Rescheduled, Completed.

## Versioning Rule
Never silently overwrite important published timetable history. A revision must preserve the old state and record who changed what, when, why, and from what effective date.

## Effective-Date Rule
Support permanent changes and temporary exceptions, including one-day room changes, date-range changes, substitutions, cancellations, and rescheduled classes.

## Conflict Management
At minimum detect:
- teacher overlap
- room overlap
- section overlap
- time overlap
- room capacity violations
- incompatible room/lab type
- duplicate active entries

Allow authorized users to fix a conflict, keep it in draft/unresolved state, or explicitly waive it with a reason.

## Cancellation Rule
Cancellation is not deletion. Preserve the original class details, affected date, reason, user, and time of cancellation.

## Non-Goals for Initial Version
No native mobile app, full ERP/LMS, microservices, or automatic AI scheduling as the first implementation.

## Technology
Python, Django, Django ORM, SQLite for development, PostgreSQL for production, HTML/CSS/JavaScript, optional Bootstrap, Git/GitHub, and GitHub Codespaces or equivalent remote development.

## Success Criteria
An authorized administrator can create/import a timetable, validate it, detect/resolve conflicts, create a tentative draft, approve/publish it, revise it later without destroying history, apply temporary exceptions, cancel/reschedule classes, notify affected users, and keep students/teachers on the correct currently effective timetable.
