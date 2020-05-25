def consonants(string):
    word = ""
    vowels = "aeiou"

    for letter in string:
        if letter not in vowels:
            word += letter
    return print(word)


consonants("Pneumonoultramicroscopicsilicovolcanoconisosis")

