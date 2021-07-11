P = float(input("Enter Principle Amount: "))

R = float(input("Enter rate of Interest: "))

T = float(input("Enter No of Years: "))

B = P * ( 1 +  R / 100)**T

print("Balance is {:.6f}".format(B))
