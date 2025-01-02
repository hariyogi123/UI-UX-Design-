# Contact book storage
contacts = []

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(f"Contact for {name} added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.\n")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"Contact {idx}:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print(f"  Address: {contact['address']}\n")

# Function to search for a contact
def search_contact():
    search_term = input("Enter name or phone to search: ")
    matches = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if matches:
        for contact in matches:
            print("\nFound Contact:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print(f"  Address: {contact['address']}\n")
    else:
        print("No contact found.\n")

# Function to edit a contact
def edit_contact():
    name_to_edit = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if name_to_edit.lower() == contact['name'].lower():
            print("Editing contact. Leave fields empty to keep current values.")
            contact['phone'] = input(f"Phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']
            print(f"Contact for {contact['name']} updated successfully.\n")
            return
    print("Contact not found.\n")

# Function to delete a contact
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if name_to_delete.lower() == contact['name'].lower():
            contacts.remove(contact)
            print(f"Contact for {name_to_delete} deleted successfully.\n")
            return
    print("Contact not found.\n")

# Main menu
def main():
    while True:
        print("Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
