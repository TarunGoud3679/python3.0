str1 = input('INPUTS \nString \n  ')
str2 = input('Word \n ')
n = str1.lower().count(str2.lower())
print("EXPECTED OUTPUT \nHow many times the search word appears in the string: {} times".format(n))
