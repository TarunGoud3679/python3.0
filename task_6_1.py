import math
cents = float(input("Enter a amount :"))
def adjust(cents):
    if cents >= 0 and cents <= 2:
        cents = 0
        return cents
    elif cents >= 3 and cents <= 7:
        cents = 5
        return cents
    elif cents >= 8 and cents <= 9:
        cents = 10
    return cents
print(adjust(cents))
