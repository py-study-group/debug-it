flag = False
number = 232792559

while flag is not True:
    for divisor in range(2,21):
        if number % divisor == 0:
            flag = True
        else:
            flag = False
            break
        break

    if flag == True:
        print(number)
        break

    number += 1
    # print(number)
