from SRP.book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            return "Book is already in collection"

    def find_book(self, title):
        book = [b for b in self.books if title == b.title]
        if book:
            return f"Book with title {title} was found"
        return "No such book"


book1 = Book("Ivan", 'ASEN')
book2 = Book("Gosho", 'ASEN')
book4 = Book("Name", 'ASEN')
book3 = Book("Ani", 'ASEN')
a = Library()
a.add_book(book1)
a.add_book(book2)
a.add_book(book3)
a.add_book(book4)
print(a.find_book("Name"))
print(a.find_book("Ads"))
book3.turn_page(book3)
print(book3.page)