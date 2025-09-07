n = int(input("Enter rows :"))
for i in range(n):
    print("*",end="")
    for j in range(n-2):
        print("_",end="")
    print("*")
      