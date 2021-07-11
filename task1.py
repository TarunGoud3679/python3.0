x = input('What is your name? ')
print('There are ' + str(len(x)) + ' characters in your name.')
a, e, i, o, u = (0,0,0,0,0)
vowela = ['a', 'A']
vowele = ['e', 'E']
voweli = ['i', 'I']
vowelo = ['o', 'O']
vowelu = ['u', 'U']
for vowel in x:
    if vowel in vowela:
        a += 1;
    elif vowel in vowele:
        e += 1;
    elif vowel in voweli:
        i += 1;
    elif vowel in vowelo:
        o += 1;
    elif vowel in vowelu:
        u += 1;
print("The number of times 'A' occurs in your name is ", a)
print("The number of times 'E' occurs in your name is ", e)
print("The numner of times 'I' occurs in your name is ", i)
print("The number of times 'O' occurs in your name is", o)
print("The number of times 'U' occurs in your name is", u)

