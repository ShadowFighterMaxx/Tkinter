def cod(arr):
    res = 0;
    for c in arr:
        res = res ^ c

    return res
def cod(arr):
    for c in arr:
        res = 0
        for d in arr:
            if c == d:
                res = res +1
        if res %2 != 0:
            return c
    return -1

arr = [];
n = int(input("enter array size"))

for c in range(n):
    num= int(input("enter the element"))
    arr.append(num)
print(arr)
print("Odd Occurence is ", cod(arr))

