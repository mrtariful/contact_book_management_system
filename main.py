from contacts import add_contact
from contacts import view_contacts
from contacts import remove_contact
from contacts import search_contact
from file_ops import load_contacts
from file_ops import save_contacts
import sys

def main_menu():
    print("\nContact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    contacts = load_contacts()
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            contacts = add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            contacts = remove_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contact saved successfully")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
