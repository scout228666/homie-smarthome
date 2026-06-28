# 🗺️ homie — Roadmap

> Development is split into milestones. Each milestone produces something working and usable — not just code.

---

## Milestone 1 — Foundation
*Backend skeleton, database, Docker*

- [ ] Project structure setup (folders, git, `.env`)
- [ ] PostgreSQL schema: `users`, `rooms`, `devices`, `sensor_readings`
- [ ] FastAPI app skeleton with Alembic migrations
- [ ] Docker + docker-compose (FastAPI + PostgreSQL)
- [ ] Cloudflare Tunnel setup for remote access
- [ ] Authentication: JWT, login page, roles (`admin` / `viewer`)

---

## Milestone 2 — Thermometer
*First real device, end-to-end*

- [ ] ESP-32 firmware: read DHT11, send data to backend via HTTP
- [ ] ESP-32 outdoor unit (sensor only)
- [ ] ESP-32 indoor unit (sensor + OLED display showing indoor & outdoor temp)
- [ ] Backend: API endpoint to receive and store readings
- [ ] Dashboard: thermometer device card (current temp & humidity)
- [ ] Thermometer detail page with historical graphs

---

## Milestone 3 — Dashboard & Rooms
*Full UI, room management*

- [ ] Main dashboard page with device cards grouped by room
- [ ] Room creation and management (admin only)
- [ ] Assign / reassign devices to rooms
- [ ] Device detail pages (generic template)
- [ ] Responsive layout (mobile-friendly for family)
- [ ] Web Push notifications (low food, temperature alerts)

---

## Milestone 4 — Pet Feeder
*Second custom device*

- [ ] ESP-32 firmware: food & water level sensors
- [ ] Backend: API endpoint for feeder readings
- [ ] Dashboard: feeder device card (food %, water %)
- [ ] Feeder detail page

---

## Milestone 5 — Third-party Integrations
*Existing home devices*

- [ ] Xiaomi vacuum — status & basic control via `python-miio`
- [ ] LG TV — status & basic control via `aiowebostv`
- [ ] LG Washing Machine — status via LG ThinQ cloud API
- [ ] Device cards and detail pages for each

---

## Milestone 6 — Polish & Portfolio
*Make it presentable*

- [ ] Demo video / GIF for README
- [ ] Screenshots of the dashboard
- [ ] Hardware schematics in `/hardware`
- [ ] Setup documentation (`docs/remote-access.md`, `docs/adding-devices.md`)
- [ ] README finalized
