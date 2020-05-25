def includes(numbers, index):
    answer = False
    for i in numbers:
        if i == index:
            answer = True
    return print(answer)

includes([20, 30, 40, 50 ,40], 60)
includes([20, 30, 40, 50 ,40], 70)
includes([20, 30, 40, 50 ,40], 30)
includes([20, 30, 40, 50 ,40], 20)
includes([20, 30, 40, 50 ,40], 50)

