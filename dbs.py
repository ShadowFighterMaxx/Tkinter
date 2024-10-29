def onTime(n):
    iteration = 0 
    for c in range(1, n+1):
        iteration+=1
    print("No of iterations is:", iteration)
n= int(input("Enter A Number"))
onTime(n) 

def onSq(n):
    iteration = 0 
    for c in range(1, n+1):
        for d in range(1, n+1):
            iteration+=1    
    print("No of iterations is:", iteration)
n= int(input("Enter A Number"))
onSq(n) 



