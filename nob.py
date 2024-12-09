def nob(n):
    count = 0
    while (n):
        count += 1
        n >>=1

        return count
    
number = int(input("Enter A Number:"))
print("Number of Hits:", nob(number))