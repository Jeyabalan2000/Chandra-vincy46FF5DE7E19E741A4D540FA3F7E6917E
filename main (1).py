def isLeapYear(year):
  if (year%4==0 and year%100             !=0) or year % 400==0: 
     return True 
  else:
    return False 

year =2025
if isLeapYear(year):
   print('{} is a leapyear.'.         format(year)) 
else:      
   print('{} is not a leap            year. '.format (year)) 
  
  