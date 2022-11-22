class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def __init__(self, book):
        self.book = book

    def format(self) -> str:
        return self.book.content


class Printer:
    def __init__(self, content):
        self.content = content

    def get_book(self):
        return f'{self.content}'


book1 = Book("IVAN")
formatter1 = Formatter(book1).format()
print(Printer(formatter1).get_book())
