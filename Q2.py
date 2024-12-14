from datetime import datetime as dt


# The decorator
def timing_decorator(func):

    def inner(*args, **kwargs):
        # run the given function with the given arguments, check current time before and after
        start = dt.now()
        result = func(*args, **kwargs)
        end = dt.now()

        # get the total running time of the function and generate an appropriate message
        time_delta = (end - start).total_seconds()
        message = f"Function '{func.__name__}' executed in {time_delta} seconds"

        # print the message and return the result of the function itself
        print(message)
        return result

    return inner


@timing_decorator
def my_sum_operation1(n):
    total = 0
    for i in range(n):
        total += i
    return total


@timing_decorator
def my_sum_operation2(n1, n2):
    total = 0
    for i in range(max(n1, n2)):
        total += i
    return total


if __name__ == '__main__':

    # Call the decorated function
    result1 = my_sum_operation1(1000000)
    print(f"Result: {result1}")
    result2 = my_sum_operation2(5000000, 66666666)
    print(f"Result: {result2}")

