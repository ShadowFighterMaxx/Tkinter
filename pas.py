num= int(input("Enter A Number"))
digits  = len(str(num))

resultNum = 0 
temp = num

while temp > 0:
    digit = temp % 10
    resultNum += digit ** digits
    temp = temp// 10

if num == resultNum:
    print("It is an Armstrong Number")

else:
    print("It is not an Armstrong Number!!")


