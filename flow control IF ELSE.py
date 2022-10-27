
############         PERCENTAGE PROBLEM          ###########
'''
per = float(input('Enter your percentage:'))
if per >= 75:
    print('You got Distinction.')
elif per >= 65:
    print('You got First class')
elif per >= 45:
    print('You got Second class')
elif per >= 35:
    print('You dont have class')
else:
    print('You are fail , need to study alot')
    ########FINDING LARGEST NUM OF THREE+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++I
''num1 = 5689
num2 = 598
num3 = 4512
if(num1>num2) and (num1>num3):
    print('The number num1 is the greatest')
elif(num2>num3):
    print('The number num2 is the greatest')
else:
    print('The number num3 is the greatest')##########Voting problem
age = int(input ('Enter the age of Individual in years:'))
if age >= 18:
    print('He is eligible for voting')
else:
    print('Not eligible')

num = int(input ('Enter the number:'))
if num%2==0:
    print('The number is divisible by 2 and even')
else:
    print('The number is not divisible by 2 and not even')
  ########   Electricity billb    ##########
    amt = 0
unit = int(input ('Enter the no. of units:'))
if unit <= 100:
    print('The total amount is', amt)
if unit>100 and unit < 201:
    amt = (unit-100)*5
    print('The total amount is', amt)
if unit>200:
    amt = (500+(unit-100)*5)
    print('The total amount is', amt)
    ############  OOOOOORRRRR
    amt = 0
unit = int(input ('Enter the no. of units:'))
if unit <= 100:
    print('The total amount is', amt)
elif unit>100 and unit < 201:
    amt = (unit-100)*5
    print('The total amount is', amt)
else:
    amt = ((100*0)+(100*5)+(unit-100)*10)
    print('The total amount is', amt)
    #############      PERCENTAGE GRADING PROBLEM  per = float(input("Enter marks obtained "))
if per > 90:
    print("Grade is A")
if per > 80 and per <=90:
    print("Grade is B")
if per >=60 and per <= 80:
    print("Grade is C")
if per < 60:
    print("Grade is D")
    ################   OOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRR per = float(input("Enter marks obtained "))
if per > 90:
    print("Grade is A")
elif per > 80 and per <=90:
    print("Grade is B")
elif per >=60 and per <= 80:
    print("Grade is C")
else:
    print("Grade is D") 
    ############PRICE OF BIKE AND TAX      
tax = 0
pr = float(input("Enter the price of bike"))
if pr > 100000:
     tax = 15/100*pr
elif pr > 50000 and pr <= 100000:
     tax = 10/100 * pr
else:
     tax = 5/100*pr
print("Tax to be paid ",tax)
#################  LEAP YEAR PROBLEM  ###################
yr=int(input("Enter the year"))
if yr%100==0:
    if yr%400==0:
          print("Entered year is leap year")
    else:
          print("Entered year is not a leap year")
else:
    if yr%4==0:
         print("Entered year is leap year")
    else:
        print("Entered year is not a leap year")
###########  NO. OF DAY AND THE DAY##########
num=int(input("Enter any number between 1 to 7 : "))
if num==1:
    print("Sunday")
elif num==2:
    print("Monday")
elif num==3:
    print("Tuesday")
elif num==4:
   print("Wednesday")
elif num==5:
   print("Thursday")
elif num==6:
   print("Friday")
elif num==2:
   print("Saturday")
else:
   print("Please enter number between 1 to 7")
##########      given delhi and answer taj mahal
                   #Delhi                               Red Fort
    #              Agra                                Taj Mahal
  #                Jaipur                              Jal Mahal
city = input("Enter name of the city from Jaipur, agra and delhi\n")
if city.casefold()=="delhi":
    print("Monument name is : Red Fort")
elif city.casefold()=="agra":
    print("Monument name is : Taj Mahal")
elif city.casefold()=="jaipur":
    print("Monument name is : Jal Mahal")
else:
    print("Enter correct name of city")
########## 3 digit number ############
num = float(input('The Number to be entered'))
if num > 99 and num < 1000:
    print('The number is 3 digit')
else:
    print('The number is not 3 digit')
##################  to find middle digit of 3-digit num###############
num1 = (input("Enter any number"))
l=len(num1)
if l != 3:
     print("Enter three digit number")
else:
     print("Middle digit is ",(int(num1)%100//10))
##########  attendance >75 eligible for exams ##########
t_num = int(input('Enter the total number of working days'))
a_num = int(input('Enter the total number of present days'))
per = a_num/t_num*100
if per >= 75:
     print('Attendance is more than 75% so eligible for Exams')
else:
     print("Can't go for exams")'''


