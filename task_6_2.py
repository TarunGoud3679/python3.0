import math


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


def roundOff(money):
    dollars = int(money)
    dec = math.modf(money)
    decimal = dec[0]
    dime = int(decimal*10)
    cents = decimal*100-int(decimal*10)*10
    fdime = dime/10
    cents = adjust(cents)
    fcents = cents/100
    arr = [dollars,fdime,fcents]
    return math.fsum(arr)


num = float(input("Enter a number : "))

print(roundOff(num))
