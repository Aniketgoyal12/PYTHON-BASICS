#Program to enter the sum of even number upto a user entered number
n = int(input("Enter the number"))
sum = 0
for i in range(1,n+1):
    if i%2 ==0:
        sum += i
print(sum)