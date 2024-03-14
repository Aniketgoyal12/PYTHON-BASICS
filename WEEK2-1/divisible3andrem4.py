#Program to check if number is divisible by 3 and last digit  is 4
n = int(input("Enter the number"))
if n % 3 == 0 and str(n)[-1] == '4':
    print("Yes")
else:
    print("No")