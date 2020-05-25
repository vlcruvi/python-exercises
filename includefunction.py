def include(list_of_numbers, index_number):
    answer = False
    for number in list_of_numbers:
        if number == index_number:
            answer = True
    return print(answer)

include([3,6,9,8,7], 6)
include([5, 6, 8, 20, 60], 21)
        