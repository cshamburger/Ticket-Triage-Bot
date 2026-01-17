import json
from pathlib import Path

DATA_FILE = Path("data/tickets.json")

def load_tickets():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_ticket(ticket):
    tickets = load_tickets()
    tickets.append(ticket)
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(tickets, f, indent=2)