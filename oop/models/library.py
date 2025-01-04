from models.rating import Rating
from models.items.library_Item import LibraryItem


class Library:
    libraries = []

    def __init__(self, name):
        self.name = name
        self._active = False
        self._ratings = []
        self._items = []
        Library.libraries.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def show_libraries(cls):
        print(f"{'Library name'.ljust(25)} | {'Rating'.ljust(25)} | Status")
        for library in cls.libraries:
            print(
                f"{str(library).ljust(25)} | {str(library.average_rating).ljust(25)} | {library.active}"
            )

    def change_status(self):
        self._active = not self._active

    @property
    def active(self):
        return "Active" if self._active else "Inactive"

    def add_rating(self, customer, rating):
        rating = Rating(customer, rating)
        self._ratings.append(rating)

    @property
    def average_rating(self):
        if not self._ratings:
            return "-"
        total_sum = sum(rating._rating for rating in self._ratings)
        average = total_sum / len(self._ratings)
        return average

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self._items.append(item)

    def show_items(self):
        print(f"Items from Library {self.name}")
        for i, item in enumerate(self._items, start=1):
            if hasattr(item, "isbn"):
                book_message = f"{i}. (Book) -> Title: {item._title.ljust(20)} | Author: {item._author.ljust(20)} | Price: {str(item._price).ljust(20)} | ISBN: {item.isbn.ljust(20)}"
                print(book_message)
            else:
                magazine_message = f"{i}. (Magazine) -> Title: {item._title.ljust(20)} | Author: {item._author.ljust(20)} | Price: {str(item._price).ljust(20)} | Edition: {item.edition.ljust(20)}"
                print(magazine_message)
