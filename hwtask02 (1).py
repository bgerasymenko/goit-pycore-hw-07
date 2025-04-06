def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

def main():
    book = AddressBook()
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
            print(add_contact(args, book))

        elif command == "change":
            name, old_phone, new_phone = args
            record = book.find(name)
            if record:
                record.edit_phone(old_phone, new_phone)
                print("Phone updated.")
            else:
                print("Contact not found.")

        elif command == "phone":
            name = args[0]
            record = book.find(name)
            if record:
                print("Phones:", ", ".join(p.value for p in record.phones))
            else:
                print("Contact not found.")

        elif command == "all":
            if not book.data:
                print("Address book is empty.")
            else:
                for name, record in book.data.items():
                    phones = ", ".join(p.value for p in record.phones)
                    bday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "N/A"
                    print(f"{name}: Phones [{phones}], Birthday [{bday}]")

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")
