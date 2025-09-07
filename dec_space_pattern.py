n = int(input("Enter rows"))
for i in range(n):
    print("*",end="")
    for j in range(i,n):
        print("_",end="")
    print("*")
      