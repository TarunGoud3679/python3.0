import array as arr
n = input("Enter num :")
num = []
lst = []
for c in n:
    num.append(int(c))
print(num)
index = [i for i, val in enumerate(num) if val != 0]
print(str(index))
index = [x - 1 for x in index]
for z in sorted(index, reverse = True):
    del num(z)
print(*num)

        
