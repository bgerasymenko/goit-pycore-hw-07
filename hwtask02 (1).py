# === ЧАТ-БОТ ===

from datetime import datetime, timedelta

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if len(phone) == 10 and phone.isdigit():
            self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)

    def add_birthday(self, bday):
        try:
            self.birthday = datetime.strptime(bday, "%d.%m.%Y")
        except:
            pass

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        return self.data.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        end_day = today + timedelta(days=7)
        result = []
        for rec in self.data.values():
            if rec.birthday:
                bday = rec.birthday.replace(year=today.year).date()
                if today <= bday <= end_day:
                    result.append(rec.name)
        return result

# === ФУНКЦІЇ ===

def parse_input(text):
    parts = text.strip().split()
    return parts[0], parts[1:]

def add_contact(args, book):
    if len(args) != 2:
        return "Use: add <name> <phone>"
    name, phone = args
    rec = book.find(name)
    if not rec:
        rec = Record(name)
        book.add_record(rec)
    rec.add_phone(phone)
    return "Contact added."

def add_birthday(args, book):
    if len(args) != 2:
        return "Use: add-birthday <name> <DD.MM.YYYY>"
    name, bday = args
    rec = book.find(name)
    if rec:
        rec.add_birthday(bday)
        return "Birthday added."
    return "Contact not found."

def show_birthday(args, book):
    name = args[0]
    rec = book.find(name)
    if rec and rec.birthday:
        return rec.birthday.strftime("%d.%m.%Y")
    return "Birthday not found."

def birthdays(args, book):
    bdays = book.get_upcoming_birthdays()
    if not bdays:
        return "No upcoming birthdays."
    return ", ".join(bdays)

def main():
    book = AddressBook()
    print("Hello! I'm your contact bot.")

    while True:
        text = input("> ")
        cmd, args = parse_input(text)

        if cmd == "exit" or cmd == "close":
            print("Bye!")
            break
        elif cmd == "hello":
            print("How can I help?")
        elif cmd == "add":
            print(add_contact(args, book))
        elif cmd == "change":
            name, old_phone, new_phone = args
            rec = book.find(name)
            if rec:
                rec.edit_phone(old_phone, new_phone)
                print("Phone changed.")
            else:
                print("Not found.")
        elif cmd == "phone":
            name = args[0]
            rec = book.find(name)
            if rec:
                print(", ".join(rec.phones))
            else:
                print("Not found.")
        elif cmd == "all":
            for name, rec in book.data.items():
                bday = rec.birthday.strftime("%d.%m.%Y") if rec.birthday else "N/A"
                print(f"{name}: {', '.join(rec.phones)} | {bday}")
        elif cmd == "add-birthday":
            print(add_birthday(args, book))
        elif cmd == "show-birthday":
            print(show_birthday(args, book))
        elif cmd == "birthdays":
            print(birthdays(args, book))
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
