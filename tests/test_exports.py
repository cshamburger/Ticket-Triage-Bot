from pathlib import Path
from src.storage import export_summary_csv, export_tickets_csv

SAMPLE = [
    {"id": 1, "description": "VPN not connecting", "priority": "P2", "group": "Network", "impact": 2, "urgency": 2, "created_at": "2026-01-17T10:00:00"},
    {"id": 2, "description": "Password reset", "priority": "P3", "group": "Service Desk", "impact": 3, "urgency": 2, "created_at": "2026-01-17T10:05:00"},
]

def test_export_summary_csv_creates_file(tmp_path: Path):
    out = tmp_path / "summary.csv"
    path = export_summary_csv(SAMPLE, output_path=str(out))
    assert Path(path).exists()
    content = Path(path).read_text(encoding="utf-8")
    assert "total_tickets" in content
    assert "priority" in content
    assert "group" in content

def test_export_tickets_csv_creates_file(tmp_path: Path):
    out = tmp_path / "tickets.csv"
    path = export_tickets_csv(SAMPLE, output_path=str(out))
    assert Path(path).exists()
    content = Path(path).read_text(encoding="utf-8")
    assert "description" in content
    assert "priority" in content
    assert "group" in content
