#Program to read three angles and tell the type of triangle
a1 = int(input("Enter the ange"))
a2 = int(input("Enter the ange"))
a3 = int(input("Enter the ange"))
if a1 + a2 + a3 == 180:
    if a1 == 90 or a2 == 90 or a3 == 90:
        print("Right Angled triangle")
    elif a1 > 90 or a2 > 90 or a3 > 90:
        print("Obtuse angle triangle")
    elif a1 < 90 or a2 < 90 or a3 < 90:
        print("Acute angled triangle")