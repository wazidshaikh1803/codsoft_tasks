# Simple Contact Book

contacts = []

while True:
    print("\n----- CONTACT BOOK MENU -----")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # Add a new contact
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact added!")

    elif choice == '2':
        # View all contacts
        if len(contacts) == 0:
            print("No contacts saved yet.")
        else:
            print("\nAll Contacts:")
            for i in range(len(contacts)):
                print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")

    elif choice == '3':
        # Search for a contact by name or phone number
        if len(contacts) == 0:
            print("No contacts saved yet.")
        else:
            search_term = input("Enter name or phone number to search: ")
            found = False

            for contact in contacts:
                if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                    print("\nContact Found:")
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print(f"Address: {contact['address']}")
                    found = True

            if not found:
                print("No matching contact found.")

    elif choice == '4':
        # Update an existing contact
        if len(contacts) == 0:
            print("No contacts saved yet.")
        else:
            for i in range(len(contacts)):
                print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")
            contact_num = int(input("Enter the contact number to update: "))

            if 1 <= contact_num <= len(contacts):
                print("Leave blank to keep the current value.")

                new_name = input(f"Enter new name ({contacts[contact_num - 1]['name']}): ")
                new_phone = input(f"Enter new phone ({contacts[contact_num - 1]['phone']}): ")
                new_email = input(f"Enter new email ({contacts[contact_num - 1]['email']}): ")
                new_address = input(f"Enter new address ({contacts[contact_num - 1]['address']}): ")

                if new_name != "":
                    contacts[contact_num - 1]['name'] = new_name
                if new_phone != "":
                    contacts[contact_num - 1]['phone'] = new_phone
                if new_email != "":
                    contacts[contact_num - 1]['email'] = new_email
                if new_address != "":
                    contacts[contact_num - 1]['address'] = new_address

                print("Contact updated!")
            else:
                print("Invalid contact number.")

    elif choice == '5':
        # Delete a contact
        if len(contacts) == 0:
            print("No contacts saved yet.")
        else:
            for i in range(len(contacts)):
                print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")
            contact_num = int(input("Enter the contact number to delete: "))

            if 1 <= contact_num <= len(contacts):
                removed = contacts.pop(contact_num - 1)
                print(f"Deleted contact: {removed['name']}")
            else:
                print("Invalid contact number.")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 6.")