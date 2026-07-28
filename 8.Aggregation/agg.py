#Agregation represent the relationship between one or more independent objects

class Library:
    def __init__(self, name):
        self.name = name
        self.list = []
        
    def lib_name(self):
        print(self.name)

    def add_book(self, book):
        self.list.append(book)

    def list_book(self):
        for book in self.list:
            print(f"{book.name} by {book.author}")

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def list_details(self):
        print(f"{self.name} by {self.author}")

library = Library("Library of Congress Washington, D.C")

book1 = Book("Industrial Society and its revolution", "Ted Kaczynski")
book2 = Book("Atomic Habits", "Some James guy")
book3 = Book("Savita Bhabi", "Puneet Agrawal")

book1.list_details()
book2.list_details()
book3.list_details()

library.lib_name()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\n")

library.list_book()