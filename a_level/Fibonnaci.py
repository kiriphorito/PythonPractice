# def fib(index):
#     if index == 0:
#         return 0
#     elif index == 1:
#         return 1
#     return fib(index - 1) + fib(index - 2)
#
# print(fib(8))

# def fib(index, array):
#     if index < len(array):
#         # If we have already calculated the value, for that index.
#         # Just return it
#         return array[index]
#     else:
#         result = fib(index - 1, array) + fib(index - 2, array)
#         array.append(result)
#         return result
#
# array = [0,1]
# print(fib(8, array))

# pre_Value = 0
# value = 1
# newValue = 0
# counter = 0
#
# index = 8
#
# while counter < index - 1:
#     newValue = pre_Value + value
#     pre_Value = value
#     value = newValue
#     counter += 1
#
# print(value)

def fib(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        num1 = 0
        num2 = 1
        for x in range (1, pos):
            temp = num2
            num2 = num2 + num1
            num1 = temp
        return num2


print(fib(8))