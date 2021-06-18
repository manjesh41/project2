 #Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
#Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
#• a year is always a leap year if its number is exactly divisible by 400

year = int(input("Enter a year: "))
if year / 4:
    print(f'{year} is a leap year')
    if year / 100:
        print(f'{year} is  not exactly leap year')
        if year/400:
            print(f"{year} is a leap year")

else:
    print(f"{year} is common year")
