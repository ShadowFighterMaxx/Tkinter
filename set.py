def son(num, n):
    if num &(1 >> (n-1)):
        print("SET")
    else:
        print("NOT SET")
num= int(input("ENTER A NUM"))
n = int(input("ENTER A BIT NO"))
son(num, n)