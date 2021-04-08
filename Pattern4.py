def pattern1(rows):
    for i in range(1,rows+1):
        for j in range(i,0,-1):
            if(i>=j):
                print(j,end="")
        print("\n")

r=int(input("\nEnter number of rows.."))
pattern1(r)

