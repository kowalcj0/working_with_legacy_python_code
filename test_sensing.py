from abc import ABC, abstractmethod


class Display(ABC):

    @abstractmethod
    def show_line(self, line: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_last_displayed_line(self) -> str:
        raise NotImplementedError


class ArtR56Display(Display):

    def show_line(self, line: str) -> None:
        # ... use some library to show line on a real display
        pass

    def get_last_displayed_line(self) -> str:
        # some crazy code to get the last displayed line on a real display
        pass


class Sale:

    def __init__(self, display: Display) -> None:
        self.display = display

    def scan(self, barcode: str) -> None:
        item_name = self.get_item_name(barcode)
        price = self.get_price(barcode)
        item_line = f"{item_name}: £{price}"
        self.display.show_line(item_line)

    @staticmethod
    def get_item_name(barcode: str) -> str:
        # more code to get the item name by barcode
        return "Fruit salad"

    @staticmethod
    def get_price(barcode: str) -> float:
        # get price by barcode
        return 3.99









class FakeDisplay(Display):

    last_displayed_line: str = None

    def show_line(self, line: str) -> None:
        self.last_displayed_line = line

    def get_last_displayed_line(self) -> str:
        return self.last_displayed_line


def test_sale() -> None:
    fake_display = FakeDisplay()

    sale = Sale(fake_display)
    sale.scan("4 029758 682357")

    assert fake_display.get_last_displayed_line() == f"Fruit salad: £3.99"
