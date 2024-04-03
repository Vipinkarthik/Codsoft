contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully.")
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("---- Contact List ----")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("----------------------")
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['phone']:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("----------------------")
            found = True
    if not found:
        print("No matching contacts found.")
def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")
def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")
def main():
    while True:
        print("\n----- Contact Book Menu -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
