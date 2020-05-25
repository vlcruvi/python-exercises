
def largest_num(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return print(largest)


largest_num([1, 2, 5, 3, 4])
largest_num([15, 20, 50, 35, 40])
