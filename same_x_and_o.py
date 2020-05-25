

def same_x_and_o(string):
    number_of_x = 0
    number_of_y = 0
    compa = bool
    for letter in string:
        if letter.lower() == "x":
            number_of_x += 1
            print("x " + str(number_of_x))
        elif letter.lower() == "o":
            number_of_y += 1
            print("o " + str(number_of_y))
    compa = (number_of_x == number_of_y)
    return print(compa)


same_x_and_o("xxooo")
same_x_and_o("lasxxxooss")
same_x_and_o("ksadjfooashdxx")
same_x_and_o("xxoo")
