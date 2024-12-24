def pot(num):
    if num == 0:
        return 0;  
    if ((num & ~(num-1))== num):
        return 1
    return 0;

num = int(input("Enter"))

if pot(num):
    print("yes")
else:
    print("no")