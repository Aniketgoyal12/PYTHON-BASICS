#Program to convert temperature into celsius farheneit and kelvin
temp = int(input("Enter the temperature in farhenit"))
cels = 32 + temp*(9/5)
kelvin = 273  + temp
print(f"{temp} farheneit is equal to {cels} celsius and {kelvin} kelvin")