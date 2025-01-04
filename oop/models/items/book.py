from models.items.library_Item import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, author, price, isbn, pages=0):
        super().__init__(title, author, price)
        self.isbn = isbn
        # self.pages = pages

    def __str__(self):
        return f"{self._title} by {self._author}"

    def apply_discount(self):
        self._price -= self._price * 0.10  # 10% discount
