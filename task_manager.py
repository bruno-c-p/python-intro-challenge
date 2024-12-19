contacts = []

def find_contact(contact_index, contacts):
    try:
        normalized_index = int(contact_index) - 1
        if 0 <= normalized_index < len(contacts):
            return contacts[normalized_index]
    except (ValueError, TypeError):
        print("Invalid contact index. Please provide a valid number.\n")
    return None

def print_contact(index, contact):
    try:
        favorite = "⭐" if contact["favorite"] else ""
        contact_name = contact.get("name", "Unknown")
        contact_phone = contact.get("phone", "No phone")
        contact_email = contact.get("email", "No email")
        print(f"{index}. [{favorite}]\n Name: {contact_name}\n Phone: {contact_phone}\n Email: {contact_email}\n")
    except AttributeError:
        print(f"Invalid contact format for contact at index {index}.\n")

def add_contact(name, phone, email, contacts, favorite=False):
    if not all([name, phone, email]):
        print("Failed to add contact. Name, phone, and email are required.\n")
        return False
    contact = {
        "name": name.strip(),
        "phone": phone.strip(),
        "email": email.strip(),
        "favorite": favorite
    }
    contacts.append(contact)
    print(f"Contact '{name}' successfully added!\n")
    return True


def list_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
        return
    print("Contacts List:")
    for index, contact in enumerate(contacts, start=1):
        print_contact(index, contact)
    print()

def update_contact(contact_index, new_name=None, new_phone=None, new_email=None, contacts=None):
    contact = find_contact(contact_index, contacts)
    if contact is None:
        print(f"Contact {contact_index} not found. Update failed.\n")
        return False
    contact["name"] = new_name if new_name is not None else contact["name"]
    contact["phone"] = new_phone if new_phone is not None else contact["phone"]
    contact["email"] = new_email if new_email is not None else contact["email"]
    print(f"Contact {contact_index} updated successfully to: {contact}\n")
    return True

def toggle_favorite_contact(contact_index, contacts):
    contact = find_contact(contact_index, contacts)
    if contact is None:
        return
    contact["favorite"] = not contact["favorite"]
    action = "added to" if contact["favorite"] else "removed from"
    print(f"Contact {contact['name']} was {action} favorites!\n")

def list_favorite_contacts(contacts):
    favorites = [(index, contact) for index, contact in enumerate(contacts, start=1) if contact["favorite"]]
    if not favorites:
        print("No favorite contacts found.\n")
        return
    print("Favorite Contacts:")
    for index, contact in favorites:
        print_contact(index, contact)
    print()

def delete_contact(contact_index, contacts):
    contact = find_contact(contact_index, contacts)
    if contact is None:
        print(f"Contact {contact_index} not found. Unable to delete.\n")
        return False
    contacts.remove(contact)
    print(f"Contact {contact['name']} (index {contact_index}) removed!\n")
    return True

def display_menu():
    print("\nContact Manager Menu:")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Update contact")
    print("4. Add/Remove favorite")
    print("5. List favorites")
    print("6. Delete contact")
    print("7. Exit")
    return input("Choose one option: ")

def get_contact_index(contacts, action="select"):
    list_contacts(contacts)
    try:
        contact_index = int(input(f"Enter the contact number to {action}: "))
        if 0 < contact_index <= len(contacts):
            return contact_index
        else:
            print("Invalid contact number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def handle_add_contact(contacts):
    name = input("Contact name: ")
    phone = input("Contact phone: ")
    email = input("Contact email: ")
    add_contact(name, phone, email, contacts)

def handle_update_contact(contacts):
    contact_index = get_contact_index(contacts, "update")
    if contact_index:
        new_name = input("New contact name: ")
        new_phone = input("New contact phone: ")
        new_email = input("New contact email: ")
        update_contact(contact_index, new_name, new_phone, new_email, contacts)

def handle_toggle_favorite(contacts):
    contact_index = get_contact_index(contacts, "toggle favorite")
    if contact_index:
        toggle_favorite_contact(contact_index, contacts)

def handle_delete_contact(contacts):
    contact_index = get_contact_index(contacts, "delete")
    if contact_index:
        delete_contact(contact_index, contacts)

while True:
    choice = display_menu()
    if choice == "1":
        handle_add_contact(contacts)
    elif choice == "2":
        list_contacts(contacts)
    elif choice == "3":
        handle_update_contact(contacts)
    elif choice == "4":
        handle_toggle_favorite(contacts)
    elif choice == "5":
        list_favorite_contacts(contacts)
    elif choice == "6":
        handle_delete_contact(contacts)
    elif choice == "7":
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option from the menu.")
