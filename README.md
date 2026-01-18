![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-009688?logo=fastapi)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![Pytest](https://img.shields.io/badge/Tests-pytest-brightgreen?logo=pytest)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker)
![Fly.io](https://img.shields.io/badge/Deployed%20on-Fly.io-purple)
![License](https://img.shields.io/badge/License-MIT-green)


# Ticket Triage Bot

**Ticket Triage Bot** is a production-ready FastAPI service that simulates an IT Service Management (ITSM) incident triage workflow.  
It analyzes incident details, assigns priority levels, routes tickets to the appropriate support groups, and persists records using SQLite.

The project is designed to demonstrate backend API design, ITSM logic, persistence, automated testing, and cloud deployment.

---

## 🚀 Features

- RESTful API built with **FastAPI**
- Automatic incident priority calculation (P1–P4)
- Rule-based assignment group routing
- Persistent storage using **SQLite** (Fly.io volume-backed)
- Search and filter tickets by:
  - Priority
  - Assignment group
  - Keyword
- Export ticket data and summaries as CSV reports
- Fully documented API with Swagger (`/docs`)
- Automated test coverage with **pytest**
- Deployed to **Fly.io** with persistent storage

---

## 🧠 Skills & Concepts Demonstrated

- Backend API development (FastAPI)
- ITSM concepts (incident priority & routing)
- SQLite database design and persistence
- Environment-based configuration
- Automated testing (pytest + TestClient)
- CSV report generation
- Dockerized deployments
- Cloud infrastructure (Fly.io volumes & secrets)

---

## 🗂 Project Structure

```text
src/
  api.py         # FastAPI application & routes
  triage.py      # Priority calculation & routing logic
  storage.py     # Database access & queries
  db.py          # SQLite initialization & connection
tests/
  test_api.py
  test_priority.py
  test_filters.py
  test_exports.py
data/
  tickets.db     # SQLite database (runtime / volume-backed)
reports/
  (generated CSV exports)

  ---

## 🔮 Future Enhancements

Planned improvements to evolve this project into a more advanced ITSM platform:

- Authentication & role-based access (Admin / Agent / Viewer)
- SLA tracking and breach alerts
- Ticket status lifecycle (Open, In Progress, Resolved, Closed)
- Full-text search optimization
- Web-based frontend dashboard (React or Next.js)
- Metrics & observability (request latency, ticket volume trends)
- Multi-region database replication
- CI/CD pipeline with GitHub Actions
- Optional PostgreSQL backend for larger-scale deployments

These enhancements would further align the system with enterprise ITSM tools such as ServiceNow and Jira Service Management.

