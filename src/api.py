from fastapi import FastAPI, Query
from typing import List, Optional
from src.triage import calculate_priority, assign_group
from src.storage import (
    load_tickets,
    save_ticket,
    filter_by_priority,
    filter_by_group,
    search_by_keyword,
    export_summary_csv,
    export_tickets_csv,
)
from datetime import datetime

app = FastAPI(
    title="Ticket Triage API",
    description="REST API for ticket triage, routing, and reporting",
    version="1.0.0",
)

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Ticket Triage Bot</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #0f172a;
                    color: #e5e7eb;
                    padding: 40px;
                }
                a {
                    color: #38dbf8
                    text-decoration: none;
                    font-weight: bold;
                }
                .card {
                    max-width: 700px;
                    margin: auto;
                    background: #030617;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Ticket Triage Bot API</h1>
                <p>FastAPI-powered IT ticket prioritization system.</p>

                <ul>
                    <li><a href="/docs">API Documentation</a></li>
                    <li><a href="/tickets">View Tickets</a></li>
                    <li><a href="/reports/export">Export CSV</a></li>
                </ul>

                <p>Status: <strong>Running</strong></p>
            </div>
        </body>
    </html>
    """


@app.get("/")
def root():
    return {"status": "Ticket Triage API running"}


@app.post("/tickets")
def create_ticket(
    description: str,
    impact: int = Query(..., ge=1, le=3),
    urgency: int = Query(..., ge=1, le=3),
):
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
        "created_at": datetime.now().isoformat(),
    }

    save_ticket(ticket)
    return ticket


@app.get("/tickets")
def get_tickets(
    priority: Optional[str] = None,
    group: Optional[str] = None,
    keyword: Optional[str] = None,
):
    tickets = load_tickets()

    if priority:
        tickets = filter_by_priority(tickets, priority)
    if group:
        tickets = filter_by_group(tickets, group)
    if keyword:
        tickets = search_by_keyword(tickets, keyword)

    return tickets


@app.get("/reports/export")
def export_reports():
    summary = export_summary_csv(load_tickets())
    tickets = export_tickets_csv(load_tickets())
    return {
        "summary_csv": summary,
        "tickets_csv": tickets,
    }
