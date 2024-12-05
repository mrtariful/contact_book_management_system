import csv

FILE_NAME = "contacts.csv"

def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts[row['Phone']] = {"Name": row['Name'], "Email": row['Email'], "Address": row['Address']}
    except FileNotFoundError:
        print("No existing contacts found. Starting fresh.")
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['Name', 'Email', 'Phone', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for phone, details in contacts.items():
            writer.writerow({"Name": details['Name'], "Email": details['Email'], "Phone": phone, "Address": details['Address']})
    print("Contacts saved successfully.")