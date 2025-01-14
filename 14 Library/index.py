print("\n")


class Library:
    def __init__(self):
        self.books = []
        self.nBook = 0

    def _addBook(self, newBook):
        self.books.append(newBook)
        self.nBook = len(self.books)

    def show(self):
        print(f"There are {self.nBook} books in Library:")
        i = 1
        for book in self.books:
            print(i, "\b]", book)
            i += 1


L1 = Library()
L1._addBook("Rich Dad Poor Dad")
L1._addBook("Psychology of Money")
L1._addBook("The Power of Your Subconscious Mind")
L1.show()

print("\n")
