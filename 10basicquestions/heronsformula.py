# Area of Triangle Using Heron's Formula where sides entered by user
s1 = int(input("Enter the side "))
s2 = int(input("Enter the side "))
s3 = int(input("Enter the side "))
#if s1 + s2 < s3 or s2 + s3 < s1 or s3 + s1 < s2 :
s = (s1+s2+s3)/2
area = ((s)*(s-s1)*(s-s2)*(s*s3))**0.5
print(area)