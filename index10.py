def multiply_by_index(numbers):
    total = 0
    for number in numbers:
        total += number * numbers.index(number)
    return print (total)

multiply_by_index([1, 2, 3])