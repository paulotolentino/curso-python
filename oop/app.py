from models.library import Library
from models.items.book import Book
from models.items.magazine import Magazine


def main():
    library1 = Library("Library 1")
    library2 = Library("Library 2")
    library3 = Library("Library 3")

    library1.change_status()
    library3.change_status()

    library1.add_rating("Customer 1", 7)
    library1.add_rating("Customer 2", 5)

    book1 = Book("Book 1", "Author 1", 10, "123-456789-0")
    book1.apply_discount()
    book2 = Book("Book 2", "Author 2", 15, "123-456789-1")
    magazine1 = Magazine("Magazine 1", "Publisher 1", 5, "First Edition")

    library1.add_item(book1)
    library1.add_item(book2)
    library1.add_item(magazine1)

    library1.show_items()

    # Library.show_libraries()


if __name__ == "__main__":
    main()
