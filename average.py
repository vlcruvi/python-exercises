def average (numbers):
    sum = 0
    result = 0.0
    for n in numbers:
        sum += n
    result = sum / len(numbers)
    return print(result)

average ([2,2,2,2,2])
    