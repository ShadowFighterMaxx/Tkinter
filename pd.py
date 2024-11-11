n = int(input("Enter A Number: "))

og = n
rg = 0

while n>0:
    digit = n % 10
    rg = rg * 10 + digit
    n//=10

if og == rg:
    print("Its a Palindrome")
else:
    print("It isnt a Palindrome")    
