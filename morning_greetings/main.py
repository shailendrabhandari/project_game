# main.py

from morning_greetings.contacts import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

def main():
    # Initialize the contacts manager
    contact_manager = Contacts()
    
    # Add some contacts
    contact_manager.add_contact("Alice", "alice@example.com")
    contact_manager.add_contact("Bob", "bob@example.com")
    contact_manager.add_contact("Charlie", "charlie@example.com")

    # Get the list of contacts
    contacts = contact_manager.get_contacts()

    # Send a message to each contact
    for contact in contacts:
        message = generate_message(contact['name'])
        send_message(contact, message)
        log_message(contact, message)

if __name__ == "__main__":
    main()

