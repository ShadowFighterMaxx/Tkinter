def nob(n):
    o = 0
    z = 0

    while(n):
        if (n&1==1):
            o+=1
        else:
            z+=1

        n>>=1
    print("Zeroes are", z, "Ones are", o)

no = int(input("enter:"))
nob(no)
