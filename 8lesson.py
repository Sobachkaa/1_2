import json

class Contact:
    def __init__(self, last_name, first_name, middle_name, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone_number = phone_number

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, index):
        del self.contacts[index]

    def find_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.last_name.lower() or query.lower() in contact.first_name.lower() or query.lower() in contact.middle_name.lower():
                results.append(contact)
        return results

    def export_to_file(self, filename):
        with open(filename, "w") as f:
            for contact in self.contacts:
                f.write(f"{contact.last_name},{contact.first_name},{contact.middle_name},{contact.phone_number}\n")

    def import_from_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                last_name = parts[0]
                first_name = parts[1]
                middle_name = parts[2]
                phone_number = parts[3]
                contact = Contact(last_name, first_name, middle_name, phone_number)
                self.contacts.append(contact)

def print_contact(contact):
    print(f"{contact.last_name}, {contact.first_name}, {contact.middle_name}, {contact.phone_number}")

def print_contact_list(contact_list):
    for contact in contact_list:
        print_contact(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти контакт")
        print("4. Вывести все контакты")
        print("5. Экспорт в файл")
        print("6. Импорт из файла")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            middle_name = input("Отчество: ")
            phone_number = input("Номер телефона: ")
            contact = Contact(last_name, first_name, middle_name, phone_number)
            contact_book.add_contact(contact)
            print("Контакт успешно добавлен")
        elif choice == "2":
            index = int(input("Введите номер контакта для удаления: "))
            contact_book.remove_contact(index-1)
            print("Контакт успешно удален")
        elif choice == "3":
            query = input("Введите запрос для поиска контакта: ")
            results = contact_book.find_contact(query)
            print_contact_list(results)
        elif choice == "4":
            contact_list = contact_book.contacts
            print_contact_list(contact_list)
        elif choice == "5":
            filename = input("Введите имя файла для экспорта: ")
            contact_book.export_to_file(filename)
            print("Контакты успешно экспортированы в файл")
        elif choice == "6":
            filename = input("Введите имя файла для импорта: ")
            contact_book.import_from_file(filename)
            print("Контакты успешно импортированы из файла")
        elif choice == "7":
            break