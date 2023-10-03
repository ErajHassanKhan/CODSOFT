class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print()

    def search_contact(self, keyword):
        matching_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                matching_contacts.append(contact)
        return matching_contacts

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

contact_book = ContactBook()

while True:
    print("******** Contact Book **********")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email: ")
        address = input("Enter the address: ")
        contact = Contact(name, phone_number, email, address)
        contact_book.add_contact(contact)
        print("Contact added successfully.\n")
    elif choice == '2':
        if not contact_book.contacts:
            print("No contacts to display.\n")
        else:
            print("Contacts:")
            contact_book.view_contacts()
    elif choice == '3':
        keyword = input("Enter a name or phone number to search: ")
        matching_contacts = contact_book.search_contact(keyword)
        if matching_contacts:
            print("Matching Contacts:")
            for contact in matching_contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}\n")
        else:
            print("No matching contacts found.\n")
    elif choice == '4':
        name = input("Enter the name of the contact to update: ")
        matching_contacts = contact_book.search_contact(name)
        if matching_contacts:
            new_name = input("Enter the new name: ")
            new_phone_number = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            new_address = input("Enter the new address: ")
            new_contact = Contact(new_name, new_phone_number, new_email, new_address)
            contact_book.update_contact(name, new_contact)
            print("Contact updated successfully.\n")
        else:
            print("Contact not found.\n")
    elif choice == '5':
        name = input("Enter the name of the contact to delete: ")
        matching_contacts = contact_book.search_contact(name)
        if matching_contacts:
            contact_book.delete_contact(name)
            print("Contact deleted successfully.\n")
        else:
            print("Contact not found.\n")
    elif choice == '6':
        print("Thanks for using Contact Book.")
        break
    else:
        print("Invalid choice. Please select a valid option.\n")
