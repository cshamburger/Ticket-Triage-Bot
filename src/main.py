from src.triage import create_ticket
from src.storage import (
    load_tickets,
    filter_by_priority,
    filter_by_group,
    search_by_keyword,
    export_summary_csv,
    export_tickets_csv,
)

from src.utils import clear_screen


def print_ticket(t):
    print(f"\nTicket #{t['id']} | {t['priority']} | {t['group']}")
    print(f"Description: {t['description']}")
    print(f"Impact: {t['impact']} | Urgency: {t['urgency']}")
    print(f"Created: {t.get('created_at', 'N/A')}")


def show_list(title, tickets):
    clear_screen()
    print(title)
    print("-" * len(title))
    if not tickets:
        print("\nNo matching tickets found.")
        return
    for t in tickets:
        print_ticket(t)


def menu():
    print("=== Ticket Triage Bot ===")
    print("1. Create new ticket")
    print("2. View all tickets")
    print("3. Filter by priority (P1-P4)")
    print("4. Filter by assignment group")
    print("5. Search by keyword")
    print("6. Export CSV report (summary + full export)")
    print("7. Exit")



def main():
    while True:
        clear_screen()
        menu()
        choice = input("\nSelect an option (1-7): ").strip()

        if choice == "1":
            clear_screen()
            create_ticket()
            input("\nPress Enter to continue...")
            continue

        tickets = load_tickets()

        if choice == "2":
            show_list("All Tickets", tickets)
            input("\nPress Enter to continue...")

        elif choice == "3":
            p = input("Enter priority (P1, P2, P3, P4): ").strip().upper()
            results = filter_by_priority(tickets, p)
            show_list(f"Tickets with Priority {p}", results)
            input("\nPress Enter to continue...")

        elif choice == "4":
            g = input("Enter group (Service Desk, Network, IT Support, Messaging, General Support): ").strip()
            results = filter_by_group(tickets, g)
            show_list(f"Tickets in Group: {g}", results)
            input("\nPress Enter to continue...")

        elif choice == "5":
            k = input("Enter keyword to search: ").strip()
            results = search_by_keyword(tickets, k)
            show_list(f"Search Results for: {k}", results)
            input("\nPress Enter to continue...")

        elif choice == "6":
            summary_path = export_summary_csv(tickets)
            export_path = export_tickets_csv(tickets)
            print("\nCSV export complete ✅")
            print(f"Summary: {summary_path}")
            print(f"Tickets:  {export_path}")
            input("\nPress Enter to continue...")

        elif choice == "7":
            print("Goodbye!")
            break


        else:
            print("Invalid choice.")
            input("Press Enter to retry...")


if __name__ == "__main__":
    main()
