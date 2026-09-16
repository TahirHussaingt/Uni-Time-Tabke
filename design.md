# Design System

## Product Character
Official-university portal: professional, clean, calm, modern, information-first and accessible. Timetable readability is more important than visual effects.

## Starter Colors
```css
--primary: #163A5F;
--primary-dark: #0F2944;
--accent: #2F7D8C;
--background: #F5F7FA;
--surface: #FFFFFF;
--text: #1F2937;
--muted: #6B7280;
--border: #E5E7EB;
--success: #198754;
--warning: #D97706;
--danger: #DC3545;
--info: #0D6EFD;
```
Replace these with official university branding when provided.

## Typography
`Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`

Page title: 32px desktop / 24px mobile, 700
Section: 24px, 600
Card: 18px, 600
Body: 15-16px
Metadata: 13-14px

## Timetable UI
Support weekly grid, daily view, real duration blocks, teacher, room, section, current/next class and clear changed/cancelled/rescheduled/tentative indicators.

A class such as 8:30-10:10 should appear as one continuous class block, not as two unrelated row entries.

## Status Design
Use text + icon + color for Draft, Tentative, Under Review, Approved, Published, Superseded, Cancelled, Rescheduled, Changed and Conflict. Never rely on color alone.

## Version UI
Show current published version, effective date and actions such as View, Compare, Create Revision, Submit Review, Publish and Archive.

## Change UI
Display old value, new value, effective date, reason, changed by and publication status.

## Conflict UI
Display conflict type, affected resources, existing/proposed entries, overlap and severity. Allow authorized Fix, Keep Draft, Details and Waive actions.

## Cancellation UI
Show `CANCELLED`, original details, reason and optional replacement information. Cancellation must not look like deletion.

## Dashboards
Student/Teacher priority: current class -> next class -> today -> latest change -> weekly timetable -> notifications.

Admin priority: timetable status -> conflicts -> pending approvals -> recent changes -> current version -> quick actions -> reports.

## Navigation
Student: Dashboard, My Timetable, Today, Courses, Notifications, Announcements, Profile.

Teacher: Dashboard, My Timetable, Today, Courses, Rooms, Notifications, Announcements, Report Issue, Profile.

Admin: Dashboard, Students, Teachers, Academic Structure, Courses, Rooms, Time Slots, Timetable, Conflicts, Changes/History, Notifications, Announcements, Reports, Settings.

## Accessibility
Semantic HTML, labels, keyboard navigation, focus states, readable contrast, text+icon status indicators, accessible tables and meaningful controls.

## Responsive Design
Desktop is the primary admin environment. Mobile prioritizes current class, next class, today, notifications and a usable timetable view.

## Branding
Keep university name, logo, colors and favicon configurable rather than hard-coded throughout templates.
