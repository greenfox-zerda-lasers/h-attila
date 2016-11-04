numbers = [4, 5, 6, 7, 8, 9, 10]
numbers_2 = [4, 6, 8, 22, 765, 7567474, 42342, 5643567]


# write your own sum function

def my_sum(input_numbers):
    sum = 0
    for i in input_numbers:
        sum += i
    print("A vegosszeg:", sum)


my_sum(numbers)
my_sum(numbers_2)