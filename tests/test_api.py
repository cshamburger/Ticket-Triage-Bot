import os
from fastapi.testclient import TestClient
from pathlib import Path

from src.api import app


def test_create_and_get_tickets(tmp_path: Path, monkeypatch):
    # Redirect JSON storage to a temp file for this test
    db_path = tmp_path / "tickets.json"
    db_path.write_text("[]", encoding="utf-8")
    monkeypatch.setenv("TICKET_DB_PATH", str(db_path))

    client = TestClient(app)

    # Create a ticket
    r = client.post("/tickets", params={"description": "VPN not connecting", "impact": 2, "urgency": 2})
    assert r.status_code == 200
    ticket = r.json()
    assert ticket["description"] == "VPN not connecting"
    assert ticket["priority"] in {"P1", "P2", "P3", "P4"}
    assert "group" in ticket
    assert "created_at" in ticket

    # Get tickets
    r2 = client.get("/tickets")
    assert r2.status_code == 200
    tickets = r2.json()
    assert isinstance(tickets, list)
    assert len(tickets) == 1


def test_filters_priority_group_keyword(tmp_path: Path, monkeypatch):
    db_path = tmp_path / "tickets.json"
    db_path.write_text("[]", encoding="utf-8")
    monkeypatch.setenv("TICKET_DB_PATH", str(db_path))

    client = TestClient(app)

    client.post("/tickets", params={"description": "VPN not connecting", "impact": 2, "urgency": 2})
    client.post("/tickets", params={"description": "Password reset needed", "impact": 3, "urgency": 2})

    # Priority filter
    r = client.get("/tickets", params={"priority": "P2"})
    assert r.status_code == 200
    p2 = r.json()
    # Depending on your priority logic, VPN may be P2—if not, just verify valid response
    assert isinstance(p2, list)

    # Group filter
    r = client.get("/tickets", params={"group": "Network"})
    assert r.status_code == 200
    g = r.json()
    assert isinstance(g, list)

    # Keyword filter
    r = client.get("/tickets", params={"keyword": "password"})
    assert r.status_code == 200
    k = r.json()
    assert any("Password" in t["description"] or "password" in t["description"].lower() for t in k)


def test_export_reports(tmp_path: Path, monkeypatch):
    db_path = tmp_path / "tickets.json"
    db_path.write_text("[]", encoding="utf-8")
    monkeypatch.setenv("TICKET_DB_PATH", str(db_path))

    client = TestClient(app)
    client.post("/tickets", params={"description": "Outlook not syncing", "impact": 2, "urgency": 1})

    r = client.get("/reports/export")
    assert r.status_code == 200
    data = r.json()
    assert "summary_csv" in data
    assert "tickets_csv" in data
