def pattern1(length):
    number=1
    for i in range(1,length+1):
        for j in range(1,length+1):
            if(i>=j):
                print(number," ",end="")
                number+=1
            else:
                pass
        print("\n")

r=int(input("\nEnter number of rows.."))
pattern1(r)