def largest(list_of_the_user):
    greatest_number = 0
    for number in list_of_the_user: 
        if number > greatest_number:
            greatest = number
    return print(greatest)



largest([2, 3, 4, 5])
largest([20, 30, 50, 40, 60])