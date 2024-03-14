#a program that converts a given number of seconds into hours, minutes, and seconds
time = int(input("Enter the number of seconds"))
hours = time //3600
minutes = time //60
print(f"{time} is equal to {hours} hours and {minutes} minutes")