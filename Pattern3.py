def pattern1(rows):
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            if(i<=j):
                print(i,end="")
        print("\n")

r=int(input("\nEnter number of rows.."))
pattern1(r)

