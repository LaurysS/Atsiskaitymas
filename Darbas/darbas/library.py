

class Library:
    def __init__(self):
        self.file_manager = FileManager()
        self.books = self.file_manager.load_books()
        self.users = self.file_manager.load_users()

    def add_book(self, pavadinimas, autorius, metai, zanras, kiekis):
        new_book = Book(pavadinimas, autorius, metai, zanras, kiekis)
        self.books.append(new_book)
        self.save_books()

    def remove_old_books(self, year_limit):
        self.books = [book for book in self.books if book.metai >= year_limit]
        self.save_books()
        print(f"Senos knygos iki {year_limit} metų ištrintos.")

    def find_books(self, pavadinimas=None, autorius=None):
        found_books = []
        for book in self.books:
            if (pavadinimas and pavadinimas.lower() in book.pavadinimas.lower()) or (autorius and autorius.lower() in book.autorius.lower()):
                found_books.append(book)
        return found_books

    def show_books(self):
        for book in self.books:
            print(book)

    def show_overdue_books(self, user):
        overdue_books = user.get_overdue_books()
        if overdue_books:
            print(f"{user.name} Turi vėluojančias atiduoti knygas: {', '.join(overdue_books)}")
        else:
            print(f"{user.name} skaitytojas neturi vėluojančiu atiduotu knygų.")

    def save_books(self):
        self.file_manager.save_books(self.books)

    def save_users(self):
        self.file_manager.save_users(self.users)

    def register_user(self, name):
        if name not in [user.name for user in self.users]:
            new_user = User(name)
            self.users.append(new_user)
            self.save_users()
            return new_user
        return next(user for user in self.users if user.name == name)
