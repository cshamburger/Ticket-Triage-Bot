## Ticket Triage Bot

Python-based ITSM simulation that analyzes incident details to assign priority,
route tickets to support groups, and store records for workflow automation practice.

---

### Features
- Create and manage incident tickets via CLI
- Automatic priority assignment (P1–P4)
- Rule-based assignment group routing
- Search and filter tickets by priority, group, or keyword
- Export timestamped daily CSV reports (summary + full ticket list)
- Automated test coverage with pytest

---

### Skills Demonstrated
- Python CLI development
- ITSM logic (priority & routing)
- JSON persistence
- Modular architecture
- Input validation & automated testing
- CSV report generation

---

### Project Structure
```text
src/
  main.py        # CLI entry point
  triage.py      # Business logic
  storage.py     # Persistence & CSV exports
  utils.py       # Helpers
tests/
  test_priority.py
  test_filters.py
  test_exports.py
data/
  tickets.json
reports/
  (generated at runtime)
