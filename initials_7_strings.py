def initials(whole_name):
    result = ""
    initial = True
    for letter in whole_name:
        if initial:
            result += letter
            initial = False
        elif letter == " ":
            initial = True
    return print(result)

initials("Vinicius Cruvinel")