def leap(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
print(f"{year} is a leap year" if leap(year) else f"{year} is not a leap year")