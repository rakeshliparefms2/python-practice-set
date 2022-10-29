'''######## MARKED PRICE AND DISCOUNT PROBLEM
m_price = int(input('Enter marked price'))
if m_price <= 7000:
    t_price = m_price*90/100
    print('The total price of product after discount is', t_price)
elif m_price > 7000 and m_price <= 10000:
    t_price = m_price*85/100
    print('The total price of product after discount is', t_price)
else:
    t_price = m_price*80/100
    print('The total price of product after discount is', t_price)
######## do all numeric operation using programming
num_1 = int(input('Enter First number'))
num_2 = int(input('Enter Second number'))
op = input('The mathematical operator:')
if op =='+' :
    print('The mathematical operation is addition', num_1+num_2)
elif op =='-' :
    #print('The mathematical operation is Subtration', num_1- num_2)
elif op =='*' :
    print('The mathematical operation is Multiplication', num_1*num_2)
elif op =='/' :
    print('The mathematical operation is Division', num_1/num_2)
elif op =='**' :
    print('The mathematical operation is Exponential', num_1**num_2)
else:
    print('The mathematical operation is Floor Division', num_1//num_2)
########## POSSIBILITY OF TRIAANGLE IFF SSIIDES ARE GIVEN
s1 = int(input('First side of any triangle'))
s2 = int(input('Second side of any triangle'))
s3 = int(input('Third side of any triangle'))
if  s2 + s3 > s1:
    print('Triangle is possible')
elif s1 + s3 > s2:
    print('Triangle is possible')
elif s1 + s2 > s3:
    print('Triangle is possible')
else:
    print('Triangle is not possible')
######## GREATEST OF 2 NUMBERS
n1 = int(input('Enter the first number'))
n2 = int(input('Enter the Second number'))
if n1 > n2:
    print('The greatest number is', n1)
else:
    print('The greatest number is', n2)
####### GREATEST OF 3 NUMBERS
n1 = int(input('Enter the first number'))
n2 = int(input('Enter the Second number'))
n3 = int(input('Enter the Third number'))
if n1 > n2 and n1 > n3:
    print('The greatest number is', n1)
elif n2 > n1 and n2 > n3:
    print('The greatest number is', n2)
elif n3 > n2 and n3 > n1:
    print('The greatest number is', n3)
else:
    print('not possiible')
#check whether number +ve,-Ve or zero
num = int(input('Enter the number'))
if num > 0:
    print('The number is Positive and number is', num)
elif num < 0:
    print('The number is Negative and number is', num)
else:
    print('The number is zero')
######### CHECK WHETHER ALPHABET OR NUMBER
a = (input('Enter the value'))
if a.isalpha() == True:
    print('It is alphabet')
elif a.isnumeric() == True:
    print('It is digit')
else:
    print('It is neither alphabet nor digit')
########## HOW TO GUESS VOOWEL OR CONSONANT IN STR
s = input('Enter any alphabet')
vowels = ['a', 'i','e', 'o', 'u']
if s in vowels:
    print('IS vowel')
else:
    print('Is consonants')
    #######  alphabet in upper or lower case
s = input('Enter the Alphabet\n')
if s.isalpha() == True:
    if s.isupper() == True:
     print('The alphabet is in upper case')
    else:
     print('The alphabet is in lowercase')
else:
    print('The character entered is not alphabet')

########## TO COUNT TOTAL NO. OF NOTES IN GIVEN AMOUNT ###############


s = int(input('Enter the amount whose count is to be done'))
if s%2000 == 0:
    print('The total notes count = ', s/2000)
else:
    print('Count of Rs. 2000 notes ', s//2000)
    x = s-(s//2000*2000)
    if x%500 == 0:
        print('The total notes count = ',x/500)
    else:
        print('Count of Rs. 500 notes ', x//500)
    x1 = x-(x//500*500)
    if x1%200 == 0:
        print('The total notes count = ', x1/200)
    else:
        print('Count of Rs. 200 notes ', x1//200)
    x2 = x1-(x1//200*200)
    if x2 % 100 == 0:
        print('The total notes count = ', x2 / 100)
    else:
        print('Count of Rs. 100 notes ', x2// 100)
    x3 = x2 - (x2 // 100 * 100)
    if x3 % 50 == 0:
        print('The total notes count = ', x3 / 50)
    else:
        print('Count of Rs. 50 notes ', x3// 50)
    x4 = x3 - (x3 // 50 * 50)
    if x4 % 20 == 0:
        print('The total notes count = ', x4 / 20)
    else:
        print('Count of Rs. 20 notes ', x4 // 20)
    x5 = x4 - (x4 // 20 * 20)
    if x5 % 10 == 0:
        print('The total notes count = ', x5 / 10)
    else:
        print('Count of Rs. 10 notes ', x5 // 10)
    x6 = x5 - (x5 // 10 * 10)
    if x6 % 5 == 0:
        print('The total notes count = ', x6 / 5)
    else:
        print('Count of Rs. 5 notes ', x6 // 5)
    x7 = x6 - (x6 // 5 * 5)
    if x7 % 2 == 0:
        print('The total notes count = ', x7 / 2)
    else:
        print('Count of Rs. 2 notes ', x7 // 2)
    x8 = x7 - (x7 // 2 * 2)
    if x8 % 1 == 0:
        print('The total notes count of Rs 1 = ', x8 / 1)
    else:
        print('Count of Rs. 1 notes ', x8 // 1)

########  state whether triangle possible or not if angles are given
a1 = int(input('The First angle=', ))
a2 = int(input('The Second angle=', ))
a3 = int(input('The Third angle=', ))
if (a1+a2+a3)==180:
    print('The triangle is possible')
else:
    print('The trianngle not possible')

######### Isosceles , Equilateral OR Scalene Triangle
a1 = int(input('The First side=',))
a2 = int(input('The Second side=',))
a3 = int(input('The Third side=',))
if a1==a2==a3:
    print('The triangle is Equilateral')
elif a1!=a2!=a3:
    print('The triangle is Scalene')
else:
    print('The triangle is Isosceles')
#######       PROFIT OR LOSS percentage
cp = int(input('The cost price is =',))
sp = int(input('The Sslling Price is =',))
if ((sp-cp)/cp)*100 > 0:
    print('The profit is ', ((sp-cp)/cp)*100)
else:
    print(('The Loss is ', ((cp - sp) / sp) * 100))

########### prcentage and grade of pcmbc
a1 = int(input('PHY marks=',))
a2 = int(input('CHEM marks=',))
a3 = int(input('MATHS marks=',))
a4 = int(input('BIO marks=',))
a5 = int(input('COMP marks=',))
x = (a1+a2+a3+a4+a5)/500*100
a = 'Grade A'
b = 'Grade B'
c = 'Grade C'
d = 'Grade D'
e = 'Grade E'
f = 'Grade F'
if x >= 90:
    print('The Percentage is {} and Grade is {}'.format(x,a))
elif x >= 80 and x < 90:
    print('The Percentage is {} and Grade is {}'.format(x,b))
elif x >= 70 and x < 80:
    print('The Percentage is {} and Grade is {}'.format(x,c))
elif x >= 60 and x < 70:
    print('The Percentage is {} and Grade is {}'.format(x,d))
elif x >= 40 and x < 60:
    print('The Percentage is {} and Grade is {}'.format(x,e))
else:
    print('The Percentage is {} and Grade is {}'.format(x,f))

########## BASIC SALARY AND GROSSS SALARY
b_s = int(input('Basic salary of employee is ='))
if b_s <= 10000:
    g_s =(b_s*20/100 + b_s*80/100)
    print('The gross salary of Employee is =', g_s)
elif b_s <= 20000 and b_s > 10000:
    g_s = (b_s * 30 / 100 + b_s * 90 / 100)
    print('The gross salary of Employee is =', g_s)
elif b_s > 20000:
    g_s = (b_s * 35 / 100 + b_s * 95 / 100)
    print('The gross salary of Employee is =', g_s)
else:
    print('Please enter correct salary')

############### ELECTRICITY CHARGES BILL
nu = int(input('No. of electricity units is ='))
if nu >= 0 and nu <= 50:
    e_b = nu*0.5*1.17
    print('The total electricity bill is =', e_b)
elif nu>50 and nu<=150:
    e_b = ((50*0.5) + (nu-50)*0.75)*1.17
    print('The total electricity bill is =', e_b)
elif nu>150 and nu<=250:
    e_b = ((50 * 0.5) + (100 * 0.75) + (nu - 150) * 1.25) * 1.17
    print('The total electricity bill is =', e_b)
elif nu> 250:
    e_b = ((50 * 0.5) + (100 * 0.75) + (100 * 1.25) + (nu - 250) * 1.5) * 1.17
    print('The total electricity bill is =', e_b)
else:
    print('Enter correct nu')'''
