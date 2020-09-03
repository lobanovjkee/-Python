from abc import ABC, abstractmethod


class Apparel(ABC):
    @abstractmethod
    def coat_size(self):
        pass

    @abstractmethod
    def suit_height(self):
        pass


class Coat(Apparel):
    def __init__(self, size):
        self.size = size

    @property
    def coat_size(self):
        fabric_length = self.size / 6.5 + 0.5
        return fabric_length

    def suit_height(self):
        pass


class Suit(Apparel):
    def __init__(self, height):
        self.height = height

    @property
    def suit_height(self):
        fabric_length = 2 * self.height + 0.3
        return fabric_length

    def coat_size(self):
        pass


coat = Coat(52)
suit = Suit(180)
print(coat.coat_size)
print(suit.suit_height)
