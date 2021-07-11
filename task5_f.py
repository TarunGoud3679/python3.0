num = input("Enter two or more numbers as a string to find the average of only even numbers out of them : ")  # input
nums = num.split('0') #split with zeros

nums = [int(i) if i else 0 for i in nums] #nums in integer

f = [i for i,x in enumerate(nums) if not x] #index of nulls from split

re = list(map(int, f)) #integers values list of above line
r = 0
re2 = []

for r in range(len(re)):          # syntax of code
    if r >= 0:
        h = re[r] - re[r-1]          
        if h == 1:
            re[r] = re[r-1]
            
            re1 = re[r] - 1
            re2.append(re1)
        
        elif re[r] == re[r]:
            re1 = re[r] - 1
            re2.append(re1)
for k in range(len(num)):
    for m in range(len(re2)):
        if k == re2[m]:
            nums[k] *= 10

no = list(map(str, nums))
even = [num for num in nums if num % 2 == 0]

length = len(even) - len(re2)
average = sum(even) / length


print("Average is : ""{:.2f}" .format(average))
