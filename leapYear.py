# conditions:
#for leap year 
# 1. (ya to 400 se divide hona chaheye ) or (nai to 4 se divede ho and 100 se divide na ho)
# else not a leap year

year = int(input("Enter year: "))
if (year%400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
   print("LEAP YEAR!")
else:
   print("NOT A LEAP YEAR")

#by function
def Is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
year = int(input("Enter Year: "))
print(Is_leap_year(year))


# Default function to implement conditions to check leap year  
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0 and  
     Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year")  
# Taking an input year from user  
Year = int(input("Enter the number: "))  
# Printing result  
CheckLeap(Year)  
