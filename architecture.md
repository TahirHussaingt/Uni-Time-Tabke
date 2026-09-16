# Architecture - University Timetable Management System

## Architecture Style
Use a **modular Django monolith** initially.

Browser -> URLs -> Views/Forms -> Services/Validation/Permissions -> Django ORM -> Database

Do not introduce microservices unless an actual requirement appears.

## Django Apps
- `accounts` - authentication, roles, permissions
- `students` - student profiles and section membership
- `teachers` - teacher profiles, availability and assignments
- `academics` - departments, programs, sessions, semesters, sections
- `courses` - courses and course offerings/assignments
- `rooms` - buildings, rooms, capacity, room/lab capability
- `timetable` - versions, entries, intervals, overrides, conflicts, changes, publication
- `notifications` - in-app notifications
- `announcements` - university notices
- `reports` - reporting/export
- `audit` - important audit events

## Initial Structure
```text
university-timetable/
├── README.md
├── architecture.md
├── rules.md
├── phases.md
├── design.md
├── memory.md
├── .gitignore
├── .env.example
├── requirements.txt
├── manage.py
├── config/
├── apps/
│   ├── accounts/
│   ├── students/
│   ├── teachers/
│   ├── academics/
│   ├── courses/
│   ├── rooms/
│   ├── timetable/
│   ├── notifications/
│   ├── announcements/
│   ├── reports/
│   └── audit/
├── templates/
├── static/
├── media/
├── scripts/
└── docs/
```

## Core Models
Identity: `User`, `StudentProfile`, `TeacherProfile`

Academic: `Department`, `Program`, `AcademicSession`, `Semester`, `Section`

Courses: `Course`, `CourseOffering`/`CourseAssignment`

Rooms: `Building`, `Room`, `RoomCapability`, `RoomAvailability`

Scheduling: `TimeSlot` (optional display concept), `TimetableVersion`, `TimetableEntry`, `TimetableOverride`, `TimetableChange`, `Conflict`, `PublicationRecord`

Communication: `Notification`, `Announcement`

Audit: `AuditEvent`

## TimetableVersion
Represents a coherent schedule version for an academic scope. Suggested concepts: version number, academic session, scope, status, created by, reviewed by, approved by, published at, effective_from, effective_to, previous_version, notes and change summary.

## TimetableEntry
Represents an actual teaching activity. Store course offering, teacher, section, room, weekday/date rule, **start_time**, **end_time**, effective dates, status, recurring/non-recurring flag and notes.

Never assume that a visible PDF row equals the actual class duration. The source contains multi-row intervals such as 8:30-10:10 and 3:10-4:50.

## TimetableOverride
Used for one-day/date-range exceptions: room, teacher, time, cancellation, extra/replacement class, etc. The normal recurring schedule should remain intact when an exception is temporary.

## TimetableChange
Record affected entry/version, change type, old values, new values, reason, requested_by, approved_by, timestamps, effective dates and notification status.

Types can include `TIME_CHANGED`, `DAY_CHANGED`, `ROOM_CHANGED`, `TEACHER_CHANGED`, `SECTION_CHANGED`, `COURSE_CHANGED`, `CANCELLED`, `RESCHEDULED`, `SUBSTITUTE_ASSIGNED`, `RESTORED`.

## Conflict
Store type, affected entries, severity, status, detection/resolution timestamps, resolver and resolution notes.

Statuses: Open, Acknowledged, Resolved, Waived. A waiver requires authorized human action and a reason.

## Publication Flow
Draft -> Validate -> Conflict Scan -> Review -> Approve -> Publish -> Active -> Superseded -> Archived

A new published version must not destroy the previous version.

## Change Flow
Admin edits -> validate -> compare old/new -> create change/revision/override -> approval if required -> effective/publish -> notify users -> audit.

## Current Schedule Resolution
Identify the user -> find currently effective published version -> apply applicable date-specific overrides/cancellations -> return effective schedule -> determine current/next class.

## Import Flow
Upload CSV/Excel -> Parse -> Normalize -> Preview -> Validate -> Conflict Scan -> Create Draft -> Review -> Publish.
