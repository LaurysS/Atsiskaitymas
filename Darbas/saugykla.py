import json
import os
import datetime
from book import Book
from vartotojas import User

class Saugykla:
    def __init__(self, books_file='Knygos.json', users_file='Vartotojai.json'):
        self.books_file = books_file
        self.users_file = users_file

    def save_books(self, books):
        with open(self.books_file, 'w') as f:
            json.dump([book.__dict__ for book in books], f)  #saugo failus dict formatu

    def load_books(self):
        if not os.path.exists(self.books_file):
            return []
        try:   
            with open(self.books_file, 'r') as f:
                books_data = json.load(f)
                return [Book(**book_data) for book_data in books_data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Klaida užkraunant biblioteka: {e}")
            return []
        

    def save_users(self, users):
        with open(self.users_file, 'w') as f:
            users_data = {}
            for user in users:
                borrowed_books = {}
                for book, due_date in user.borrowed_books.items():
                    if isinstance(due_date, datetime.date):
                        borrowed_books[book] = due_date.strftime('%Y-%m-%d')  
                    else:
                        borrowed_books[book] = due_date
                users_data[user.name] = {
                    "Knyga paimta": borrowed_books
                }
            json.dump(users_data, f)

    def load_users(self):
        if not os.path.exists(self.users_file): #patikrina ar egzistuoja failas
            return []

        try:
            with open(self.users_file, 'r') as f:
                users_data = json.load(f)
                users = []
                for user_name, data in users_data.items():
                    user = User(user_name)
                    borrowed_books = {}
                    for book, due_date in data['Knyga paimta'].items():
                        if due_date:
                            borrowed_books[book] = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
                    user.borrowed_books = borrowed_books
                    users.append(user)
                return users
        except (json.JSONDecodeError, IOError) as e:
            print(f"Klaida ieškant vartotojo: {e}")
            return []
