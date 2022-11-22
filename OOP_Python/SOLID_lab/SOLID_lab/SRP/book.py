from SRP.turn_page import TurnPage


class Book(TurnPage):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0
