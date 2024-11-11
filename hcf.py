nl = int(input("enter the largest no:"))
sl = int(input("enter the smallest no:"))

while(sl):
    nos = sl
    sl = nl% sl
    nl = nos

print("HCF is", nl)