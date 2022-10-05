from book import Book
from borrowingOrder import BorrowingOrder
from client import Client
from librarian import Librarian


def MainMenu():

        choice = input("\n\tMain Menu\n"
                       "1. Clients Menu\n"
                       "2. Librarian Menu\n"
                       "3. Books Menu\n"
                       "4. Borrowing Orders Menu\n"
                       "5. Exit the System\n"
                       "Your choice: ")

        if choice == "1":
            Client.ClientsMenu()
            MainMenu()

        if choice == "2":
            Librarian.LibrariansMenu()
            MainMenu()

        elif choice == "3":
            Book.BooksMenu()
            MainMenu()

        elif choice == "4":
            BorrowingOrder.OrdersMenu()
            MainMenu()

        elif choice == "5":
            exit("\nSystem is closed.")

        else:
            print("\nInvalid input!")
            MainMenu()

MainMenu()