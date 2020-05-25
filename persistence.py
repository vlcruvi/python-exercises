def persistence(numbers):
    total_numbers = 0
    multiplication_numbers = 0
    iterations = 0
    digit_1 = True
    string_number = str(numbers)
    while digit_1:
        for number in string_number:
            total_numbers += int(number)
        iterations += 1
        print(total_numbers)
        string_number = str(total_numbers)
        if len(str(total_numbers)) < 2:
            print(len(str(total_numbers)))
            return
        total_numbers = 0
    return print(str(iterations))
            

persistence(12345)

