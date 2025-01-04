from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price
        # self._checked_out = False
        # self._ratings = []

    @abstractmethod
    def apply_discount(self):
        pass
