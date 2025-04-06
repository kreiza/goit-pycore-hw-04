def parse_input(user_input: str) -> tuple:
    """
    Parse the user input into a command and its arguments.

    :param user_input: The raw input string entered by the user.
    :return: A tuple containing the command (str) and a list of arguments.
    """
    parts = user_input.split()
    if not parts:
        return "", []
    command = parts[0].strip().lower()
    args = parts[1:]
    return command, args


def add_contact(args: list, contacts: dict) -> str:
    """
    Add a new contact to the contacts dictionary.

    :param args: A list where the first element is the contact's name and the second is the phone number.
    :param contacts: The dictionary storing contacts (name: phone).
    :return: A confirmation message or an error message if arguments are insufficient.
    """
    if len(args) < 2:
        return "Insufficient arguments for add command."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list, contacts: dict) -> str:
    """
    Update an existing contact's phone number.

    :param args: A list where the first element is the contact's name and the second is the new phone number.
    :param contacts: The dictionary storing contacts.
    :return: A message indicating whether the contact was updated or not found.
    """
    if len(args) < 2:
        return "Insufficient arguments for change command."
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args: list, contacts: dict) -> str:
    """
    Retrieve and return the phone number for a given contact.

    :param args: A list where the first element is the contact's name.
    :param contacts: The dictionary storing contacts.
    :return: The contact's phone number or a message if the contact is not found.
    """
    if not args:
        return "No name provided for phone command."
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts: dict) -> str:
    """
    Return all saved contacts and their phone numbers.

    :param contacts: The dictionary storing contacts.
    :return: A string representation of all contacts and their phone numbers.
    """
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """
    Run the CLI assistant bot, processing commands from the user.

    The bot supports commands: hello, add, change, phone, all, exit/close.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
