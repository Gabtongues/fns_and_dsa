size=int(input("enter the size of the pattern."))
if size<=0:
    print("please enter a posiitive interger pattern size.")
else:
    row_count=0
    while row_count<size:
        for _ in range(size):
            print("*", end="")
            row_count+=1
except ValueError:
print("invalid input, please enter an interger")
