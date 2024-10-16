from library import Library
from vartotojas import User
from book import Book
import datetime
import json


def main():
    library = Library()

    while True:
        print("\nSveiki prisijungė prie Lauryno bibliotekos!")
        print("1. Prisijungti kaip bibliotekininkas")
        print("2. Prisijungti kaip skaitytojas")
        print("3. Uždaryti biblioteka")
        choice = input("Pasirinkite norimą meniu laukeli: ")

        if choice == '1':
            library_menu(library)
        elif choice == '2':
            reader_name = input("Įveskite savo vardą: ")
            reader = library.register_user(reader_name)
            reader_menu(library, reader)
        elif choice == '3':
            print("Viso gero!")
            break
        else:
            print("Tokio meniu pasirinkimo nėra.")

def library_menu(library):
    while True:
        print("\nBibliotekos meniu")
        print("1. Pridėti knygą")
        print("2. Išimti senas knygas")
        print("3. Peržiūrėti visas knygas")
        print("4. Grįžti į pagrininį meniu lnagą")
        choice = input("Pasirinkite norimą meniu laukeli: ")

        if choice == '1':
            pavadinimas = input("Pavadinimas: ")
            autorius = input("Autorius: ")
            while True:
                try:
                    metai = int(input("Metai: "))
                    if 1500 <= metai <= 2024:
                        break
                    else:
                        print("Netinkamas metai. Prašau įvesti metus tarp 1500 ir 2024.")
                except ValueError:
                            print("Įvestas netinkamas formatas. Prašome įvesti sveiką skaičių.")
            # metai = int(input("Metai: "))
            zanras = input("Žanras: ")
            while True:
                try:
                    kiekis = int(input("Knygų kiekis: "))
                    if kiekis <= 0:
                        print("Kiekis negali būti neigiamas. Prašome įvesti teigiamą skaičių.")
                    else:
                        break
                except ValueError:
                            print("Įvestas netinkamas formatas. Prašome įvesti sveiką skaičių.")
            library.add_book(pavadinimas, autorius, metai, zanras, kiekis)
            print(f"Knyga '{pavadinimas}' pridėta į biblioteką.")
        elif choice == '2':
            year_limit = int(input("Išimti knygas senesnes nei: "))
            library.remove_old_books(year_limit)
        elif choice == '3':
            library.show_books()
        elif choice == '4':
            break
        else:
            print("Tokio meniu pasirinkimo nėra.")

def reader_menu(library, reader):
    while True:
        print(f"\nSkaitytoju meniu - {reader.name}")
        print("1. Pasiimti knygą")
        print("2. Grąžinti knygą")
        print("3. Ieškoti knygos iš sąrašo")
        print("4. Peržiūrėti vėluojančias atiduoti knygas")
        print("5. Išeiti")
        choice = input("Pasirinkite norimą meniu laukeli: ")

        if choice == '1':
            knygos_pavadinimas = input("Įveskite norimos knygos pavadinimą: ")
            due_date = datetime.date.today() + datetime.timedelta(days=10) # laiko limitas kiek galima laikyti knyga
            books = library.find_books(pavadinimas=knygos_pavadinimas)
            if books:
                books[0].borrow(reader, due_date)
                library.save_users() #išsaugoma user faile duomenys papie skaitytoja
            else:
                print(f"Knygos '{knygos_pavadinimas} sąraše nėra'.")
        elif choice == '2':
            knygos_pavadinimas = input("Kokia knygą norite grąžinti: ")
            books = library.find_books(pavadinimas=knygos_pavadinimas)
            if books:
                books[0].return_book(reader)
                library.save_users()  #išsaugoma user faile duomenys papie skaitytoja
            else:
                print(f"Knygos '{knygos_pavadinimas} sąraše nėra'.")
        elif choice == '3':
            search_title = input("Įveskite ieškomos knygos pavadinimą (ar dalį jo): ")
            search_author = input("Įveskite autoriaus vardą (ar dalį jo): ")
            books = library.find_books(pavadinimas=search_title, autorius=search_author)
            if books:
                for book in books:
                    print(book)
            else:
                print("Knygą nerasta.")
        elif choice == '4':
            library.show_overdue_books(reader)
        elif choice == '5':
            break
        else:
            print("Neteisingas pasirinkimo variantas.")

if __name__ == '__main__':
    main()
