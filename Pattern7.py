def pattern1(n):
    for i in range(0,n//2+1): #IT WILL RUN UPTO 4 ROWS WHEN n=7 BECAUSE n//2=3,
        for j in range(0,n):                                 #AND 3+1=4 ROWS
            if((j>=i)and(j<=n-i-1)) :
                print("@",end="")
            else:
                print(" ",end="")
        print("\n")

n=int(input("\nEnter any number..."))
pattern1(n)