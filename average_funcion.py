def average(list_of_numbers):
    average = 0.0
    sum_of_items_of_the_list = 0
    for i in list_of_numbers:
        sum_of_items_of_the_list += i
    average = sum_of_items_of_the_list / len(list_of_numbers)
    return print(average)

average([2,2,2,2,2,2,2,2,2,2,2,2])