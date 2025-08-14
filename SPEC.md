# Time Clock System Specification

## Key features

- Mobile PWA time clock with geofencing
- Automatic overtime calculations according to Israeli law (125% for first 2 overtime hours, 150% thereafter)
- Shift thresholds: default 42-hour week (5×8.6h) and options for 6‑day week
- Night shifts flagged when at least 2 hours fall between 22:00–06:00
- Weekend/Holiday rest day compensation (175–200%) with optional rest-day replacement
- Break deduction of 45 minutes for workdays longer than 6 hours (configurable)
- Geofence check only on clock‑in/out, storing hashed location (geohash) to protect privacy; no continuous tracking
- Optional kiosk mode with PIN/QR for devices without GPS
- Configurable policies: daily & weekly thresholds, automatic break deduction, rest day compensation
- Export payroll data (CSV/Excel/API) and integration with payroll systems
- Role-based access: Employee (clock in/out, view times, request corrections), Manager (approve corrections & overtime), Admin (configure sites, policies, geofences and holidays)
- Audit log for all changes and exports; privacy by design with data minimization and retention settings
