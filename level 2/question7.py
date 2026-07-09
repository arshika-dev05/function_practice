# create a function that takes year as input and check leap year.
def leap_year(year):

    if year % 400==0 :
        print("leap year")
    elif year % 100==0:
        print(" not a leap year")
    elif year % 4==0:
        print("leap year")    
    else:
        print("not a leap year")
 

year=int(input("enter year="))
leap_year(year)