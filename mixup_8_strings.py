def mixup(word1, word2):  
    first_new_word = word2[0] + word1[1:] 
    second_new_word = word1[0] + word2[1:]
    result = first_new_word + " " + second_new_word
    return print(result)


mixup("Kelvin", "Alex")