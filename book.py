class Book:

    def __init__(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status


    bookList = []


    def BooksMenu():

        isReturn = False
        while (not isReturn):

            choice = input("\n\tBooks Menu\n"
                           "1. Add new book\n"
                           "2. Delete book\n"
                           "3. View book\n"
                           "4. List all books\n"
                           "5. Total available books\n"
                           "6. Total borrowed books\n"
                           "7. Return to main menu\n"
                           "Your choice: ")

            if choice == "1":
                Book.AddBook()

            elif choice == "2":
                Book.DeleteBook()

            elif choice == "3":
                Book.ViewBook()

            elif choice == "4":
                Book.ListBooks()

            elif choice == "5":
                Book.TotalAvailable()

            elif choice == "6":
                Book.TotalBorrowed()

            elif choice == "7":
                isReturn = True

            else:
                print("\nInvalid input!")


    def SearchBook(id):

        for book in Book.bookList:
            if book.id == id:
                return book.bookList.index(book)
        return -1

    def ActiveBooks():

        print("\nActive Books:")
        print("\nBook id\t Book title\t Book description\t Book author\t Book status")
        for book in Book.bookList:
            if book.status == "Active":
                print(book.id, "\t", book.title, "\t", book.description, "\t", book.author, "\t",
                      book.status)


    def AddBook():

        id = input("\nEnter book id: ")
        if id.strip() != '' and id.isdigit() and Book.SearchBook(id) == -1:
            title = input("Enter book title: ")
            if title.strip() != '':
                description = input("Enter book description: ")
                if description.strip() != '':
                    author = input("Enter book author: ")
                    if author.strip() != '' and author.replace(' ', '').isalpha():
                        status = "Active"

                        newBook = Book(id, title, description, author, status)
                        Book.bookList.append(newBook)
                        print("\nBook added successfully\n")

                    else:
                        print("\nInvalid input!\n")
                else:
                    print("\nInvalid input!\n")
            else:
                print("\nInvalid input!\n")
        else:
            print("\nInvalid input!\n")

        isReturn = False
        while (not isReturn):

            again = input("Do you want to add another book?\n"
                          "1. Yes\n"
                          "2. No\n"
                          "Your choice: ")
            if again == "1":
                Book.AddBook()
            elif again == "2":
                isReturn = True
            else:
                print("\nInvalid input!\n")


    def DeleteBook():

        bookId = input("\nEnter the book id you want to delete.\n"
                       "id: ")
        index = Book.SearchBook(bookId)
        if index != -1:
            Book.bookList.pop(index)
            print("\nBook deleted successfully\n")
        else:
            print("\nThere is no book with this id\n")

        isReturn = False
        while (not isReturn):

            again = input("Do you want to delete another book?\n"
                          "1. Yes\n"
                          "2. No\n"
                          "Your choice: ")
            if again == "1":
                Book.DeleteBook()
            elif again == "2":
                isReturn = True
            else:
                print("\nInvalid input!\n")


    def ViewBook():

        id = input("\nEnter a book id to view its data\n"
                   "id: ")
        index = Book.SearchBook(id)

        if index != -1:
            print("Book id\t Book title\t Book description\t Book author\t Book status")
            print(Book.bookList[index].id, "\t", Book.bookList[index].title, "\t",
                  Book.bookList[index].description, "\t", Book.bookList[index].author, "\t",
                  Book.bookList[index].status)

        else:
            print("\nInvalid input!")

        isReturn = False
        while (not isReturn):

            choice = input("\nDo you want to view another book:\n"
                           "1. Yes\n"
                           "2. No\n"
                           "Your choice: ")
            if choice == "1":
                Book.ViewBook()
            elif choice == "2":
                isReturn = True
            else:
                print("Invalid input!\n")


    def ListBooks():

        if len(Book.bookList) > 0:
            print("\nBook id\t Book title\t Book description\t Book author\t Book status")
            for book in Book.bookList:
                print(book.id, "\t", book.title, "\t", book.description, "\t", book.author, "\t",
                      book.status)
        else:
            print("\nThere are no registered books yet")


    def TotalAvailable():

        active = 0
        for book in Book.bookList:
            if book.status == "Active":
                active = active + 1
        print("\nTotal available book = ", active)


    def TotalBorrowed():

        inactive = 0
        for book in Book.bookList:
            if book.status == "Inactive":
                inactive = inactive + 1
        print("\nTotal borrowed book = ", inactive)