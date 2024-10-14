import datetime

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book, due_date):
        self.borrowed_books[book.pavadinimas] = due_date
        print(f"{self.name} pasiėmė knygą '{book.pavadinimas}' iki {due_date}.")

    def return_book(self, book):
        if book.pavadinimas in self.borrowed_books:
            del self.borrowed_books[book.pavadinimas]
            print(f"{self.name} grąžinote '{book.pavadinimas}'.")

    def has_overdue_books(self):
        today = datetime.date.today()
        for due_date in self.borrowed_books.values():
            if today > due_date:
                return True
        return False

    def get_overdue_books(self):
        today = datetime.date.today()
        overdue = [book for book, due_date in self.borrowed_books.items() if today > due_date]
        return overdue
