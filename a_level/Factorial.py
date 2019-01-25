# Notes
# DON'T USE INPUT! It's a reserved keyword
# So the format of "range" in for loops are range (Starting value, exclusive ending value, step)
# Each "block" whether it maybe an if block or a for block requires a colon ':' to represent the start of block

# Python Conventions
# Names of function are lowercase. So instead of uppercasing a letter to say new word, you you underscore to space words
# Two lines between every class and every method


def factorial_for_increment(in_value):
    result = 1
    for i in range (2 , in_value + 1 , 1):
        result = result * i
    return result


def factorial_for_decrement(in_value):
    result = in_value
    for i in range (in_value - 1 , 1 , -1):
        result = result * i
    return result


def factorial_recursion(in_value):
    if in_value == 1:
        return 1
    else:
        return in_value * factorial_recursion(in_value - 1)


def factorial(in_value):
    if in_value == 0:
        return 0
    elif in_value < 0:
        print("Cannot do negative factorial")
    else :
        print("The factorial of ", in_value, "is:")
        print("FactorialForIncrement: ", factorial_for_increment(in_value))
        print("FactorialForDecrement: ", factorial_for_decrement(in_value))
        print("factorialRecursion: ", factorial_recursion(in_value))


x = 3
factorial(x)