p = int(input("Enter the size of triangle:"))
x=int(p)

for i in range(x):
  for j in range(x-i):
    print("* ",end="")
  print()
