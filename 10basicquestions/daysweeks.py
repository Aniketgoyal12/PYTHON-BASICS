#Program to convert year into days weeks and months
year = int(input("Enter the number of years"))
months = year *12
weeks = year *52
days = year * 365
print(f"{year} has {days} days {months} months {weeks} weeks")