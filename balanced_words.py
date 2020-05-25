#We can assign a value to each character in a word, 
#based on their position in the alphabet (a = 1, b = 2, 
#... , z = 26). A balanced word is one where the sum of 
#values on the left-hand side of the word equals the sum 
#of values on the right-hand side. For odd length words, 
#the middle character (balance point) is ignored.

def balanced_words(word):
    side_1 = ""
    side_2 = ""
    word_1= ""
    word_2 =""
    sum_1 = 0
    sum_2 = 0
    if int(len(word)) % 2 == 0:
        side_1 = word[0:int(len(word)/2)]
        side_2 = word[int(len(word)/2):]
    else:
        side_1 = word[0:int(len(word)/2)]
        side_2 = word[int(len(word)/2)+1:]
    for letter in side_1:
        word_1 += str(ord(letter) - 96)
        sum_1 += ord(letter) - 96
    print("soma 1: " + str(sum_1))
    for letter in side_2:
        word_2 += str(ord(letter)-96)
        sum_2 += ord(letter) - 96
    print("soma 2: " + str(sum_2))
    return print(sum_1 == sum_2)

       
    #if word % 2 == 0:
    #   for letter in word:
    #      side_1 += str(ord(letter) - 96)
    return 

balanced_words("abcd")


        