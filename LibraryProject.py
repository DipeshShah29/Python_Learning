##Library class
# #displayLibrary
# issueBook

##Student Class
# requestBook
# returnBook


class Library:
    def __init__(self):
        self.booksAvailable = ["book1", "book2", "book3", "book4", "book5"]

    def displayLibrary(self):
        if len(self.booksAvailable) > 0:
            print(self.booksAvailable)
        else:
            print("There are no books available in the Library")

    def issueBook(self, bookRequested):
        if bookRequested in self.booksAvailable:
            self.booksAvailable.remove(bookRequested)
            print("Thank you! you have successfully issued", bookRequested)
            print("Available books:", self.booksAvailable)
        else:
            print("Sorry! The book you have entered is not available in the Library")

    def addBook(self, bookReturned):
        self.booksAvailable.append(bookReturned)
        print("Thank you for returning the book")
        print("Available books:", self.booksAvailable)


class Student:
    def requestBook(self):
        print("Enter the name of a book you want to borrow")
        self.bookRequested = input()
        Lib = Library()
        lib.issueBook(self.bookRequested)

    def returnBook(self):
        print("Please enter the name of a book you want to return")
        self.returnedBook = input()
        lib = Library()
        lib.addBook(self.returnedBook)


lib = Library()
stud = Student()

while True:

    print("Kindly select an option from the Library")
    print("Enter 1 to show available books in the Library")
    print("Enter 2 to issue a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    optionSelected = int(input())
    if optionSelected == 1:
        lib.displayLibrary()
    elif optionSelected == 2:
        stud.requestBook()
    elif optionSelected == 3:
        stud.returnBook()
    else:
        quit()
