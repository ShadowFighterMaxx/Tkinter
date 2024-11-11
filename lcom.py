num1 = int(input("enter a no."))
num2 = int(input("enter a no."))

for i in range(max(num1, num2), (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
    break
print ("lcm is ", lcm)
