# Intermediate Python Program: Contact Book

class ContactBook:
    def __init__(self):
        # Initialize an empty contact book
        self.contacts = {}

    def add_contact(self, name, phone):
        # Add a new contact
        if name in self.contacts:
            print(f"Contact for {name} already exists.")
        else:
            self.contacts[name] = phone
            print(f"Contact for {name} added successfully.")

    def search_contact(self, name):
        # Search for a contact by name
        if name in self.contacts:
            print(f"{name}'s phone number is {self.contacts[name]}.")
        else:
            print(f"Contact for {name} not found.")

    def delete_contact(self, name):
        # Delete a contact
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print(f"Contact for {name} not found.")

    def display_contacts(self):
        # Display all contacts
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContacts List:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")


# Main Program
if __name__ == "__main__":
    contact_book = ContactBook()
    
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == "2":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "3":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "4":
            contact_book.display_contacts()
        elif choice == "5":
            print("Exiting the contact book.")
            break
        else:
            print("Invalid option. Please try again.")
