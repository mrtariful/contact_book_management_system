from error_handling import validate_contact

def add_contact(contacts):
    print("\nAdd New Contact")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    
    if validate_contact(name, phone):
        if phone in contacts:
            print("Error: Duplicate phone number.")
        else:
            contacts[phone] = {"Name": name, "Email": email, "Address": address}
            print("Contact added successfully.")
    return contacts

def view_contacts(contacts):
    print("\nView All Contacts")
    for phone, details in contacts.items():
        print(f"Name: {details['Name']}, Email: {details['Email']}, Phone: {phone}, Address: {details['Address']}\n")

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to remove: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact removed successfully.")
    else:
        print("Error: Contact not found.")
    return contacts

def search_contact(contacts):
    query = input("Enter name, phone, or email to search: ")
    results = [f"Name: {v['Name']}, Phone: {k}, Email: {v['Email']}, Address: {v['Address']}"
               for k, v in contacts.items() if query.lower() in v['Name'].lower() or query == k or query.lower() in v['Email'].lower()]
    if results:
        print("\nSearch Results:")
        for res in results:
            print(res)
    else:
        print("No matching contacts found.")
