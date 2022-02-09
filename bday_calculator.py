import datetime


calculate = int(input("1. Age \n2. Birth Year \nEnter which option (1 or 2) you want to calculate: "))

current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day

# Birth Date Input
birth_day = int(input("Enter birth day: "))
birth_month = int(input("Enter birth month: "))


# Age Calculation
def age_calculator():
    birth_year = int(input("Enter birth year: "))

    if (diff_month < 0):
        age = current_year - birth_year - 1
    elif (diff_month > 0):
        age = current_year - birth_year
    else:
        if (diff_day >= 0):
            age = current_year - birth_year
        elif (diff_day < 0):
            age = current_year - birth_year - 1
    
    print("Your age is: ", age)


# Birth Year Calculation
def birth_year_calculator():
    age = int(input("Enter your age: "))
    # current year known so no need to ask again

    if (diff_month > 0):
        birth_yr = current_year - age    # change name of variables later
    elif (diff_month < 0):
        birth_yr = current_year - age - 1
    else:
        if (diff_day >= 0):
            birth_yr = current_year - age
        elif (diff_day < 0):
            birth_yr = current_year - age - 1

    print("Your birth year is : ", birth_yr)


diff_month = current_month - birth_month
diff_day = current_day - birth_day


if (calculate == 1):    
    age_calculator()
elif (calculate == 2):
    birth_year_calculator()
else:
    print("Invalid option input! \nPlease Try Again...")
