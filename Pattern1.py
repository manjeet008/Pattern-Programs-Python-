def pattern1(rows,columns):
    for i in range(rows):
        for j in range(columns):
            if(i%2!=0):
                if(j<i):
                    print(" ",end="")
                else:
                    print("*",end="")
            else:
                if(j<(columns-i)):
                    print("*",end="")
        print("\n")
        
rows=int(input("Enter rows here.."))
columns=int(input("Enter columns here.."))
pattern1(rows,columns)
