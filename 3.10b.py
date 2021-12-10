n=int(input("n="))
i=1
while i<=n:
    print(i,end=" ")
    if i%5==0 or i%10==0:
        print()
    i=i+1