from math import sqrt

number = int(input("Enter A Number:"))
if number > 1:
    for i in range(2, int(sqrt(number)) +1):

        if (number % 1 )== 0:
            print ("composite")
            break
        else:
            print("prime")

else:
    print("composite")    