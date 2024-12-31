def pof(n):
    count = 0;
    if(n &(~(n&(n-1)))):
        while (n>1):
            n>>=1
            count+=1

        if (count % 2 == 0):
            return True
    else:
        return False
    
n = int(input("ENTER"))

if pof(n):
    print("yes")

else:
    print("no")