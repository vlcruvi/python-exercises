'''Create a function that determines whether each seat can 
"see" the front-stage. A number can "see" the front-stage 
if it is strictly greater than the number before it.
Everyone can see the front-stage in the example below:
# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc. '''

def concert_seats(lista):
    first_element = True
    comparison = 0
    answer = True
    first_loop = True
    end_loop = 0
    counting_loop = 0
    for i in range(len(lista)):
        end_loop = len(lista[i]) 
        #print("endLoop: " + str(end_loop))
        
        for j in range(len(lista[i])):
            counting_loop += 1
            if first_element:
                comparison = lista[j][i]
                first_element = False
            if counting_loop <= end_loop: 
                print("comparison " + str(comparison))
                print("posicao lista " + str(lista[j][i]))  
                if lista[j][i] > comparison:
                    answer = False
            comparison = lista[j][i] 
       
        return 

concert_seats([[3, 3, 3], [2, 2, 2], [1, 1, 1]])


