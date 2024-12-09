def eo(n):
    if (n ^ 1 == n+1):
        return True;
    else:
        return False;

number = int(input("Enter Your Number:"))

if eo(number):
    print("It is even")
else:
    print("its odd")      