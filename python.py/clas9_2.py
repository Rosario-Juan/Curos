from functools import reduce

def sum_odd_numbers(numbers):
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    sum_of_odds = reduce(lambda x, y: x + y, odd_numbers)
    return sum_of_odds

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_odds = sum_odd_numbers(numbers_list)
print("The sum of odd numbers in the list is: ", sum_of_odds)

