from storage import save_ticket, load_tickets
from utils import get_int_input
from datetime import datetime

def calculate_priority(impact, urgency):
    if impact == 1 and urgency == 1:
        return "P1"
    elif impact <= 2 and urgency <= 2:
        return "P2"
    elif impact <= 2:
        return "P3"
    return "P4"

def assign_group(description):
    desc = description.lower()
    rules = {
        "password": "Service Desk",
        "login": "Service Desk",
        "vpn": "Network",
        "network": "Network",
        "laptop": "IT Support",
        "hardware": "IT Support",
        "email": "Messaging",
        "outlook": "Messaging"
    }
    for keyword, group in rules.items():
        if keyword in desc:
            return group
    return "General Support"

def create_ticket():
    description = input("Short description: ").strip()
    impact = get_int_input("Impact (1-3): ", 1, 3)
    urgency = get_int_input("Urgency (1-3): ", 1, 3)

    priority = calculate_priority(impact, urgency)
    group = assign_group(description)

    tickets = load_tickets()
    ticket_id = len(tickets) + 1

    ticket = {
        "id": ticket_id,
        "description": description,
        "impact": impact,
        "urgency": urgency,
        "priority": priority,
        "group": group,
        "created_at": datetime.now().isoformat()
    }

    save_ticket(ticket)

    print("\nTicket Created Successfully")
    print(f"ID: {ticket_id}")
    print(f"Priority: {priority}")
    print(f"Assigned Group: {group}")