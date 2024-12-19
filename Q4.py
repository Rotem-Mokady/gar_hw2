from typing import Union


class Sqrt:
    def __init__(self, func):
        # store the function to be decorated
        self.func = func

    def __call__(self, n1: Union[int, float], n2: Union[int, float]):
        # calculate the result of the given function with the given arguments
        result = self.func(n1, n2)

        # if the result is negative return -1, otherwise calculate and return the sqrt
        if result < 0:
            return -1
        return result ** 0.5


if __name__ == '__main__':

    @Sqrt
    def add_values(n1, n2):
        return n1 + n2


    @Sqrt
    def substract_values(n1, n2):
        return n1 - n2


    print(add_values(10, 20))
    print(add_values(10, -20))
    print(substract_values(100, 19))
    print(substract_values(10, 19))
