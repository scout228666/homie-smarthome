# 🏠 homie

> A self-hosted smart home system for monitoring and managing your home devices — built with ESP-32, FastAPI, and HTMX.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue?style=flat-square&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker)
![ESP32](https://img.shields.io/badge/ESP--32-firmware-red?style=flat-square)

---

## What is homie?

**homie** is a personal smart home platform that runs entirely on your local network. It collects data from custom ESP-32 sensors, stores it in a PostgreSQL database, and displays everything through a clean web dashboard — no cloud, no subscriptions, no third-party apps.

---

## Features

- 📊 **Real-time dashboard** — device cards grouped by room, each showing live sensor data
- 🌡️ **Temperature monitor** — current temperature & humidity with historical graphs
- 🐾 **Pet feeder** — food and water level monitoring
- 🏠 **Room management** — create rooms and assign devices to them
- 🤖 **Third-party integrations** — Xiaomi vacuum (python-miio), LG TV (aiowebostv)
- 🐳 **Docker-based** — one command to run, accessible to everyone via a shared link

---

## Tech Stack

| Layer | Technology |
|---|---|
| Microcontroller | ESP-32 |
| Backend | FastAPI + asyncio |
| Database | PostgreSQL |
| Frontend | HTMX + Jinja2 |
| Deployment | Docker + docker-compose |

---

## Project Structure

```
homie/
├── firmware/           # ESP-32 code (Arduino framework)
│   ├── thermometer/
│   └── feeder/
├── backend/            # FastAPI application
│   ├── app/
│   │   ├── api/        # route handlers
│   │   ├── models/     # database models
│   │   ├── schemas/    # Pydantic schemas
│   │   ├── services/   # business logic & device drivers
│   │   └── templates/  # Jinja2 HTML templates
│   ├── migrations/     # Alembic migrations
│   └── tests/
├── hardware/           # Schematics & 3D print files (.stl, .f3d)
├── docs/               # Architecture diagrams, setup guides
├── docker-compose.yml
└── README.md
```

---

## Getting Started

### Prerequisites

- Docker & docker-compose
- A machine at home that runs 24/7 (PC, laptop, or Raspberry Pi)
- A free [Cloudflare](https://cloudflare.com) account for remote access

### Run

```bash
git clone https://github.com/yourusername/homie.git
cd homie
cp .env.example .env
docker-compose up -d
```

The dashboard is accessible from anywhere via a Cloudflare Tunnel — no port forwarding required. Family members just open a link in their browser, no apps or VPN needed.

See [docs/remote-access.md](docs/remote-access.md) for setup instructions.

---

## Devices

### Supported

| Device | Type | Protocol |
|---|---|---|
| Custom thermometer | ESP-32 + DHT11 | Wi-Fi / HTTP |
| Custom pet feeder | ESP-32 | Wi-Fi / HTTP |
| Xiaomi vacuum | Robot vacuum | python-miio |
| LG TV | Smart TV | aiowebostv |
| LG Washing Machine | Appliance | LG ThinQ API |

### Adding a new device type

Each device type requires a driver in `backend/app/services/devices/`. Once a driver exists, new instances of that device can be added through the dashboard UI without touching the code.

---

## Dashboard

The main page shows all rooms with device cards. Each card displays a device name and its key metric at a glance.

Clicking a card opens the device detail page with full info and, where applicable, historical charts.

---

## Roadmap

See [ROADMAP.md](ROADMAP.md)

---

## License

MIT
