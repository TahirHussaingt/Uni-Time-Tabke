# Development Phases

## Phase 0 - Documentation and Repository
Create GitHub repository, add six documents, configure `.gitignore`, initialize Django, verify development server and update memory.

## Phase 1 - Base UI
Base template, branding placeholder, navigation, login layout, dashboard shell, responsive structure and error pages.

## Phase 2 - Authentication and Roles
Authentication, admin/teacher/student roles, permissions, redirects and protected views.

## Phase 3 - Academic Structure
Department, program, academic session, semester, section and relationships.

## Phase 4 - People
Student profiles, teacher profiles, university IDs and section membership.

## Phase 5 - Courses
Course, code/name, credits, course offering, teacher and section assignment.

## Phase 6 - Rooms and Time Intervals
Buildings, rooms, capacity, room type/capability, room availability, flexible actual start/end time support.

## Phase 7 - Timetable Draft and Versioning
`TimetableVersion`, `TimetableEntry`, lifecycle states, daily/weekly/section/teacher/room views.

## Phase 8 - Conflict Engine
Teacher, room and section overlap; time overlap; capacity; room/lab compatibility; duplicate active entries; conflict dashboard and resolution state.

## Phase 9 - Review and Publication
Submit draft, validate, conflict scan, approve/reject, publish, supersede previous version and publication history.

## Phase 10 - Change History
`TimetableChange`, old/new values, reasons, users, effective dates, compare versions, audit trail and authorized restoration.

## Phase 11 - Overrides, Cancellation and Rescheduling
One-day/date-range overrides, room/time/day changes, substitutions, cancellation, rescheduling, replacement classes and effective-from/effective-to.

## Phase 12 - Student Dashboard
Current/next class, today, weekly timetable, latest changes, notifications, announcements and issue reporting.

## Phase 13 - Teacher Dashboard
Current/next class, today, weekly schedule, courses, sections, rooms, changes, notifications and issue reporting.

## Phase 14 - Admin Dashboard
Active version, drafts, approvals, conflicts, changes, publication status, quick actions and reports.

## Phase 15 - Notifications
Room/teacher/time/day change, cancellation, rescheduling and published-version notifications. Start with in-app notifications.

## Phase 16 - Import/Export
CSV/Excel upload, preview, normalization, validation, conflict scan, draft creation, import history, PDF/Excel/CSV export and print view.

## Phase 17 - Reports
Student, teacher, section, room and department timetables; conflict report; change history; room usage.

## Phase 18 - Automatic Scheduling
Only after manual scheduling is reliable. Add hard/soft constraints, availability, labs, generation, validation, optimization, review and human approval.

## Phase 19 - Testing and Security
Model, authentication, permission, conflict, history, publication, override, cancellation, import, notification and security tests.

## Phase 20 - Production
PostgreSQL, environment configuration, HTTPS, static/media, backups, logs, monitoring, deployment and recovery strategy.

## Phase 21 - Future Extensions
PWA/mobile, REST API, university SSO, calendar integration, push notifications, multiple campuses, advanced optimization and attendance integration.
