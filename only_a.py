def only(list_of_strings):
    total_list = []
    for word in list_of_strings:
        if "a" in word:
            total_list.append(word)
    return print(total_list)

only(["Vinicius","Tomato", "Pineaple", "Caipirinha", "Assai"])