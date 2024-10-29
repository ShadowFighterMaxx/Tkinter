def factors(number):
    print("Number of factors of ", number, " are")
    for i in range(1, number+1):
        if number % i == 0:
            print(i)

number = int(input("Enter A Number:"))
factors(number)
