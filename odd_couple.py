def odd_couple(list_numbers):
    answer = [] 
    number_of_odds = 0
    for number in list_numbers:
        if number % 2 != 0:
            answer.append(number)
            number_of_odds += 1
        if number_of_odds == 2:
            return answer
    return answer

    
print(odd_couple([5, 4, 8, 9, 145]))
print(odd_couple([4, 6]))
print(odd_couple([]))
print(odd_couple([1, 2]))