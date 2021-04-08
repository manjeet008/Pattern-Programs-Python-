def pattern1(n):
    for i in range(n):
        for j in range(n+3):
            if(i<=n//2-1):
                if(i>=j):
                    print("*",end="")
                elif(j==n+1) and (i==n//2-1):
                    print("*",end="")
                else:
                    print(" ",end="")
            elif(i==n//2):
                print("*",end="")
            else:
                if(i+j<=n-1):
                    print("*",end="")
                elif(j==n+1) and (i==n//2+1):
                    print("*",end="")
                else:
                    print(" ",end="")
        print("")
n=int(input("\nEnter any number..."))
pattern1(n)