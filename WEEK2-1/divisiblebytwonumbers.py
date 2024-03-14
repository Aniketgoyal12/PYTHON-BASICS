#Program to check divisibilty of a number by two numbers
n = int(input("Enter the number"))
n1 = int(input("Enter the first number to check with"))
n2 = int(input("Enter the second number to check with"))
if n % n1 == 0 and n%n2 == 0 :
    print("Yes")
else:
    print("NO")