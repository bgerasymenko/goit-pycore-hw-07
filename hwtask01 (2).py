from datetime import datetime, timedelta
import random

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x = value
        else:
            self.__x = None

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self.__y = value
        else:
            self.__y = None

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[idx] = Phone(new_phone)
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, bday):
        self.birthday = Birthday(bday)

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        end_period = today + timedelta(days=7)
        result = []
        for record in self.data.values():
            if record.birthday:
                bday_this_year = record.birthday.value.replace(year=today.year).date()
                if today <= bday_this_year <= end_period:
                    result.append(record.name.value)
        return result

class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Індекс має бути 0 (x) або 1 (y).")

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Індекс має бути 0 (x) або 1 (y).")

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __call__(self, multiplier=None):
        if multiplier is None:
            return (self.coordinates.x, self.coordinates.y)
        elif isinstance(multiplier, (int, float)):
            return (self.coordinates.x * multiplier, self.coordinates.y * multiplier)
        else:
            raise TypeError("Multiplier must be a number or None.")

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.coordinates.x + other.coordinates.x
            y = self.coordinates.y + other.coordinates.y
            return Vector(Point(x, y))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.coordinates.x - other.coordinates.x
            y = self.coordinates.y - other.coordinates.y
            return Vector(Point(x, y))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.coordinates.x * other.coordinates.x + self.coordinates.y * other.coordinates.y
        return NotImplemented

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __eq__(self, other):
        return self.len() == other.len()

    def __ne__(self, other):
        return self.len() != other.len()

    def __gt__(self, other):
        return self.len() > other.len()

    def __lt__(self, other):
        return self.len() < other.len()

    def __ge__(self, other):
        return self.len() >= other.len()

    def __le__(self, other):
        return self.len() <= other.len()

class Iterable:
    def __init__(self, max_vectors, max_points):
        self.max_vectors = max_vectors
        self.max_points = max_points
        self.current_index = 0
        self.vectors = [Vector(Point(random.randrange(0, max_points + 1), random.randrange(0, max_points + 1)))
                        for _ in range(max_vectors)]

    def __next__(self):
        if self.current_index >= self.max_vectors:
            raise StopIteration
        vector = self.vectors[self.current_index]
        self.current_index += 1
        return vector

class RandomVectors:
    def __init__(self, max_vectors, max_points):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)

# ✅ Приклад використання AddressBook
book = AddressBook()
rec = Record("Alice")
rec.add_phone("0501234567")
rec.add_birthday("01.05.2000")
book.add_record(rec)
print("Upcoming birthdays:", book.get_upcoming_birthdays())

# Випадкові вектори
print("\nRandom vectors:")
vectors = RandomVectors(5, 10)
for vector in vectors:
    print(vector)

