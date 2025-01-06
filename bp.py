import math;
def pw(set, setSize):
    pws = int(math.pow(2, setSize))
    outer = 0
    inner = 0;

    for outer in range(0, pws):
        for inner in range(0, setSize):
          if((outer &(1 << inner) > 0)):
             print(set[inner], end = "")
        print("")

size = int(input("ENTER SIZE"))
set = []
for i in range(0, size):
   n= int(input("Enter no"))
   set.append(n)
pw(set, len(set))
