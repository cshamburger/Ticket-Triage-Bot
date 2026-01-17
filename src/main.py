from triage import create_ticket
from storage import load_tickets
from utils import clear_screen

def menu():
    print("=== Ticket Triage Bot ===")
    print("1. Create new ticket")
    print("2. View all tickets")
    print("3. Exit")

def main():
    while True:
        clear_screen()
        menu()
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            create_ticket()
            input("\nPress Enter to continue...")
        elif choice == "2":
            tickets = load_tickets()
            for t in tickets:
                print(f"\nTicket #{t['id']} | {t['priority']} | {t['group']}")
                print(f"Description: {t['description']}")
            input("\nPress Enter to continue...")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            input("Press Enter to retry...")

if __name__ == "__main__":
    main()