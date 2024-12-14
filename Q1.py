from typing import Union


class FruitItem:
    def __init__(self, name: str, price: Union[int, float], hours_in_time_shelf: int) -> None:
        """
        Define a fruit object.

        :param name: str.
        :param price: numeric.
        :param hours_in_time_shelf: int
        """
        # define default price
        self._default_price = 10

        self.name = name
        # replace the given price by the default if the default is greater
        self.price = self._default_price if price < self._default_price else price
        self.hours_in_time_shelf = hours_in_time_shelf

    def getPrice(self) -> Union[int, float]:
        """
        :return: numeric. Fruit's price.
        """
        return self.price

    def getShelfTime(self) -> int:
        """
        :return: int. Fruit's shelf time.
        """
        return self.hours_in_time_shelf

    def __repr__(self) -> str:
        return f"Fruit Name: {self.name}, Price: {self.price}, Shelf Time: {self.hours_in_time_shelf} hours"


class FruitBasket:
    def __init__(self):
        """
        Define a basket of fruits object.
        """
        # initialize the basket as empty
        self.fruits_list = []

    def AddFruitItem(self, fruit_item: FruitItem) -> None:
        """
        Add a fruit object to the basket.
        """
        self.fruits_list.append(fruit_item)

    def DelFruitItem(self, fruit_item: FruitItem):
        """
        Remove a fruit object to the basket.
        """
        self.fruits_list.remove(fruit_item)

    def BasketPrice(self) -> Union[int, float]:
        """
        :return: numeric. The total price of the basket
        """
        # the price is 0 if there are no fruits
        if not self.fruits_list:
            return 0
        # iterate the basket, extract the price of each item and sum all of them together
        return sum([fruit_item.price for fruit_item in self.fruits_list])

    def BasketShelfTime(self) -> int:
        # there is no time shelf if there are no fruits
        if not self.fruits_list:
            return -1
        # iterate the basket, extract the time shelf of each item and take the minimum
        return min([fruit_item.hours_in_time_shelf for fruit_item in self.fruits_list])

    def __repr__(self) -> str:
        # appropriate message if there are no fruits
        if not self.fruits_list:
            return "Empty Basket"

        # generate all lines together
        first_line_message = "Printing fruits in basket:"
        fruits_lines = [fruit_item.__str__() for fruit_item in self.fruits_list]
        lines = [first_line_message] + fruits_lines

        # represent it as str
        final_message = '\n'.join(lines)
        return final_message

    def __bool__(self) -> bool:
        # True if there is at least one fruit in the basket, False otherwise
        return bool(self.fruits_list)


class HolidayFruitBasket(FruitBasket):

    def __init__(self, greeting_holiday: str) -> None:
        """
        Define a basket of fruits plus greeting holiday object.
        :param greeting_holiday: str.
        """
        super().__init__()
        self.greeting_holiday = greeting_holiday

    def getPrice(self):
        """
        Set a new price for the basket,
        :return: numeric.
        """
        # get original basket's price
        original_price = self.BasketPrice()
        # return the price with discount of 5%
        return original_price * 0.95

    def __repr__(self):
        # add the greeting holiday to object's representation
        basket_message = super().__repr__()
        return f"{self.greeting_holiday}\n{basket_message}"


if __name__ == '__main__':

    cut_apples = FruitItem('Cut Apples', 15, 4)
    print(cut_apples)
    strawberries = FruitItem('Straberries', 22, 6)
    print(strawberries)

    b1 = FruitBasket()
    if (b1):
        print("not empty")
    else:
        print("empty")

    b1.AddFruitItem(cut_apples)
    b1.AddFruitItem(strawberries)
    print(b1)
    print(b1.BasketPrice())
    print(b1.BasketShelfTime())

    if (b1):
        print("not empty")
    else:
        print("empty")

    print("*******************")

    b3 = HolidayFruitBasket("Marry Christmas")
    b3.AddFruitItem(cut_apples)
    b3.AddFruitItem(strawberries)
    b3.AddFruitItem(strawberries)
    b3.DelFruitItem(cut_apples)
    print(b3)
    print(b3.BasketPrice())
    print(b3.BasketShelfTime())