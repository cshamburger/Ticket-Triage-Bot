import json
from pathlib import Path
from typing import List, Dict, Any
import csv
from datetime import datetime, date
from pathlib import Path
from typing import List, Dict, Any


DATA_FILE = Path("data/tickets.json")


def load_tickets() -> List[Dict[str, Any]]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return []
        return json.loads(content)


def save_ticket(ticket: Dict[str, Any]) -> None:
    tickets = load_tickets()
    tickets.append(ticket)
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2)


def filter_by_priority(tickets: List[Dict[str, Any]], priority: str) -> List[Dict[str, Any]]:
    p = priority.strip().upper()
    return [t for t in tickets if str(t.get("priority", "")).upper() == p]


def filter_by_group(tickets: List[Dict[str, Any]], group: str) -> List[Dict[str, Any]]:
    g = group.strip().lower()
    return [t for t in tickets if str(t.get("group", "")).lower() == g]


def search_by_keyword(tickets: List[Dict[str, Any]], keyword: str) -> List[Dict[str, Any]]:
    k = keyword.strip().lower()
    if not k:
        return []
    results = []
    for t in tickets:
        hay = " ".join([
            str(t.get("description", "")),
            str(t.get("group", "")),
            str(t.get("priority", "")),
        ]).lower()
        if k in hay:
            results.append(t)
    return results
def export_tickets_csv(tickets: List[Dict[str, Any]], output_path: str | None = None) -> str:

    """
    Export all tickets to a CSV file and return the output path.
    """
    if output_path is None:
        output_path = f"reports/{_daily_filename('tickets', with_time=True)}"
    out = Path(output_path)



    fieldnames = ["id", "description", "impact", "urgency", "priority", "group", "created_at"]

    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in tickets:
            writer.writerow({k: t.get(k, "") for k in fieldnames})

    return str(out)


def export_summary_csv(tickets: List[Dict[str, Any]], output_path: str | None = None) -> str:

    """
    Export a summary CSV with totals, counts by priority, and counts by group.
    Returns the output path.
    """
    if output_path is None:
        output_path = f"reports/{_daily_filename('summary', with_time=True)}"
    out = Path(output_path)



    # Counts
    total = len(tickets)
    by_priority = {}
    by_group = {}

    for t in tickets:
        p = str(t.get("priority", "")).upper()
        g = str(t.get("group", "")).strip()

        by_priority[p] = by_priority.get(p, 0) + 1
        by_group[g] = by_group.get(g, 0) + 1

    # Write CSV
    now = datetime.now().isoformat()

    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["generated_at", now])
        writer.writerow(["total_tickets", total])
        writer.writerow([])

        writer.writerow(["priority", "count"])
        for p in sorted(by_priority.keys()):
            writer.writerow([p, by_priority[p]])

        writer.writerow([])
        writer.writerow(["group", "count"])
        for g in sorted(by_group.keys(), key=lambda x: x.lower()):
            writer.writerow([g, by_group[g]])

    return str(out)

def _daily_filename(prefix: str, ext: str = "csv", with_time: bool = True) -> str:
    d = date.today().isoformat()  # YYYY-MM-DD
    if with_time:
        t = datetime.now().strftime("%H%M%S")  # 235959
        return f"{prefix}_{d}_{t}.{ext}"
    return f"{prefix}_{d}.{ext}"


