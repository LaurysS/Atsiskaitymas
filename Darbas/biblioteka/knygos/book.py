
class Book:
    def __init__(self, pavadinimas, autorius, metai, zanras, kiekis, borrowed_by=None, due_date=None):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai
        self.zanras = zanras
        self.kiekis = kiekis
        self.due_date = due_date
        self.borrowed_by = borrowed_by if borrowed_by is not None else []

    def __str__(self):
        return f"{self.pavadinimas} by {self.autorius}, {self.metai} - {self.zanras} (Bendras kiekis knygų: {self.kiekis})"

    def borrow(self, reader, due_date):
        if self.kiekis > 0 and not reader.has_overdue_books():
            self.kiekis -= 1
            self.borrowed_by = reader
            self.due_date = due_date
            reader.borrow_book(self, due_date)
        elif reader.has_overdue_books():
            print(f"{reader.name}, jūs turite negrąžintų knygų, naujos negalitė pasiimti.")
        else:
            print(f"Atsiprašome, šiuo metu neturime '{self.pavadinimas}'.")

    def return_book(self, reader):
        if self.borrowed_by == reader:
            self.kiekis += 1
            self.borrowed_by = None
            self.due_date = None
            reader.return_book(self)
