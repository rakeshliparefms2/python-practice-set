'''
QUE 1 : WRITE A PROGRAM TO FIND N NATURAL NUMBERS.

n = int(input('Enter the number whose series to complete:'))
for i in range(1,n+1):
    print(i, end = ',')
------------------------------------------------------
def nat_num(x):

    for i in range(1,x+1):
        print(i, end = ' ')
    return i
a = nat_num(25)
print()
--------------------------------------------------------------------
n = int(input("Enter the natural number"))
x =[i for i in range(1,n+1)]
print(x)
-------------------------------------------------------------
n = int(input("Enter the natural number"))
ls = range(1,n+1)
print(set(map(lambda x:x ,ls)))
===============================================================================================================
QUE 2 : WRITE A PROGRAM TO FIND N to 1 NATURAL NUMBERS.
n = int(input('Enter the number whose series to complete:'))
for i in range(n, 0,-1):
    print(i, end = ',')
-------------------------------------------------------------
def nat_num(x):

    for i in range(x, 0, -1):

    return x
a = nat_num(25)
print()
----------------------------------------------------------------
n = int(input("Enter the natural number"))
ls = list(range(n,0,-1))
print(list(map(lambda x:x , ls)))
---------------------------------------------------------------
n = int(input("Enter the natural number"))
print([ i for i in range(n,0,-1)])

=========================================================================================
QUE 3 : WRITE A PROGRAM TO PRINT ALPHABETS A-Z.
--------------------------------------------------------------------------------------------------
import string
for i in string.ascii_lowercase:
    print(i, end = ' ')

import string
for i in string.ascii_uppercase:
    print(i, end = ' ')
Ans: a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
---------------------------------------------------------------------------------
while True:
    for i in range(97,123):
        print(chr(i),end='')
    break
------------------------------------------------------------------
while True:
    for i in range(65,91):
        print(chr(i),end=' ')

        print(chr(i).lower(), end = ' ')
    break
A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p
Q q R r S s T t U u V v W w X x Y y Z z
-----------------------------------------------------
print([ chr(i) for i in range(65,91)])
--------------------------------------------------------
ls = list(range(65,91))
print(list(map(lambda x:chr(x),ls)))
=================================================================================================================
QUE 4 : WAP to print even no. till 100
`--------------------------------------------------------------
n = 0
for i in range(0,101,2):
    print(i, end = ' ')
-------------------------------------------------------
def num(n):
    ls=[]
    for i in range(1,n+1):
        if i % 2==0:
            ls.append(i)
    return ls
print(num(26))
--------------------------------------------------------
n =int(input('Enter the natural number'))
print([i for i in range(0,n+1,2)])
-------------------------------------------------------
n =int(input('Enter the natural number'))
ls = range(0,n+1,2)
print(list(map(lambda x: x,ls)))

=========================================================
QUE 5  WAP to print ODD no. till 100
------------------------------------------
def num(n):
    ls=[]
    for i in range(0,n+1):
        if i%2==1:
            ls.append(i)
    return ls
print(num(51))
-----------------------------------------
n = 1
for i in range(1,100,2):
    print(i, end = ' ')
--------------------------------------------

n = int(input('ENter the natural number'))
ls = range(0,n+1)
print(list(filter(lambda x : x%2==1,ls)))
-----------------------------------------------
n = int(input('ENter the natural number'))
print( [i for i in range(1,n+1,2)])

====================================================================================================
Que 6. sum of n natural numbers
-------------------------------------------------------------------------
def num(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(num(456))
-----------------------------------------------
n = int(input('ENter the natural '))
print(sum([i for i in range(1,n+1)]))
----------------------------------------------
from functools import reduce
n = int(input('ENter the natural '))
ls = range(1,n+1)
print(reduce(lambda x,y:x+y,ls))
------------------------------------------------
n = int(input('ENter the natural '))
sum = 0
for i in range(1,n+1):
    sum+=i
print(sum)
==================================================================================
Que 7: sum of even numbers
--------------------
i = int(input('Enter the number whose series to complete:'))
if i < 0:
    print('positive no.')
else:
    sum = 0
    for i in range(0, 51,2):
        sum += i

    print(sum, end = ' ')
------------------------------------------------------------------
def even(n):
    sum =0
    for i in range(0,n+1):
        if i % 2 == 0:
            sum += i
    return sum
print(even(56))
--------------------------------------------
n=int(input('Enter the natural number'))
print(sum([i for i in range(0,n+1,2)]))
------------------------------------------------
from functools import reduce
n=int(input('Enter the natural number'))
ls = range(0,n+1,2)
print(reduce(lambda x,y:x+y,ls))

=============================================================================================================
Que 8: SUM OF ODD NUMBERS TILL 50
i = int(input('Enter the number whose series to complete:'))
if i < 0:
    print('positive no.')
else:
    sum = 0
    for i in range(1, 50, 2):
        sum += i

    print(sum, end = ' ')
def odd(n):
    ls = 0
    for i in range(1,n+1):
        if i%2==1:
            ls += i
    return ls
print(odd(25))
------------------------------------------------
n=int(input('Enter the natural number'))
print(sum([i for i in range(1,n+1,2)]))
--------------------------------------------------
from functools import reduce
n=int(input('Enter the natural number'))
ls=range(1,n+1,2)
print(reduce(lambda x,y:x+y,ls))
=======================================================================================================
QUE 9:  MULTIPLICATION OF ANY NUMBER TILL 10 X*1 TO X*10
----------------------------------------------------------------------------------------
n = int(input('Enter the number whose table we want:'))
for i in range(1, 11):
    print('The Multiplication table is: ',n*i)
-----------------------------------------------------------------------
def mul():
    n = int(input())
    for i in range(1,11):
        print(i*n)
    #return i*n
mul()
----------------------------------------------------
n=int(input('Enter the natural number'))
print({ i:(i*n) for i in range(1,11)})
-----------------------------------------------------
n=int(input('Enter the natural number'))
ls = range(1,11)
print(list(map(lambda x:x*n,ls)))

========================================================================
QUE 10 : COUNT NUMBER OF DIGITS IN NUMBER
--------------------------------------------
n = int(input('Let the number be:'))
count = 0
while(n>0):
    count += 1
    n = n//10
print(count)
-------------------------------------------------------
def num(n):
    count = 0
    for i in str(n):
        count += 1
    return count
print(num(56865))
--------------------------------------------------------------------
n=int(input('Enter the natural number'))
print(sum([(str(i).count('')-1) for i in str(n)]))
--------------------------------------------------------------------
from functools import reduce
n=input('Enter the natural number')

print(reduce(lambda x:sum((str(x).count(''))-1), n))
====================================================================

QUE 11: FIND FIRST AND LAST DIGIT OF NUMBER
---------------------------------------------
n = int(input('Enter the number'))
x = str(n)
print('First digit of number',x[0])
print('Last digit of number', x[-1])
-----------------------------------------------
def num(n):
    return str(n)[0],str(n)[-1]
n1=int(input('Enter the natural number'))
print(num(n1))
-------------------------------------------------
n=int(input('Enter the natural number'))
print([i for i in str(n)][0],[i for i in str(n)][-1])
----------------------------------------------------------------
n=int(input('Enter the natural number'))
#print(list(map(lambda x: str(n)[0]+' '+str(n)[-1] , str(n))))
=====================================================================================================================
QUE 12: FIND sum of FIRST AND LAST DIGIT OF NUMBER

n = int(input('Enter the number'))
x = str(n)
print('Sum of First and Last digit of number',int(x[0]) + float(x[-1]))

n = float(input('Enter the number'))
p = int(n)
#print(p)
x = str(p)
#print(x)
print('Sum of First and Last digit of number',int(x[0]) + int(x[-1]))
======================================================================================================
QUE 13: FIND SWAPING of FIRST AND LAST DIGIT OF NUMBER

def swap(input_val):
    input_val = [i for i in str(input_val)]
    hold = input_val[0]
    input_val[0] = input_val[-1]
    input_val[-1] = hold
    input_val =''.join(input_val)
    return int(input_val)
print(swap(2689))
-----------------------------------------
x = int(input('Enter the number'))      b
n = str(x)
print('The swap of first n last digit is', n[-1]+n[1:len(n)-1]+n[0])

==================================================================================

QUE 14: FIND  SUM OF ALL DIGIT S OF NUMBER

x1 = int(input('Enter the number'))
x = str(x1)
sum1 = 0
for d in x:
    sum1 +=int(d)
print(sum1)
===========================================================================
QUE 15: FIND  PRODUCT OF ALL DIGITS OF NUMBER

x1 = int(input('Enter the number'))
x = str(x1)
sum1 = 1
for d in x:
    sum1 *=int(d)
print(sum1)
======================================================================
QUE 16: WRITE REVERSE OF ANY NUMBER

x1 = int(input('Enter the number'))
x = str(x1)
print(x[::-1])
====================================================
QUE 17: CHECK WHETHER NUMBER IS PALINDROME OR Not

x1 = int(input('Enter the number'))
x = str(x1)
if x == x[::-1]:
    print('The no. is palindrome')
else:
    print('not palindrome')
===========================================================
QUE 18: FREQUENCY OF EACH DIGIT IN IN INTEGER

from collections import *

x1 = int(input('Enter the number'))

freq = Counter(str(abs(x1)))
print(freq)
Ans: Enter the number : 12365412365447964799985622131
Counter({'1': 4, '2': 4, '6': 4, '4': 4, '9': 4, '3': 3, '5': 3, '7': 2, '8': 1})
=============================================================================================
QUE 19 write a digit and print it in words
------------------------------------------------------------------
n = input('Enter a number: ')
while True:
    for i in n:
        if i == '0':
            print('Zero',end=' ')
        elif i == '1':
            print('One',end=' ')
        elif i == '2':
            print('Two',end=' ')
        elif i == '3':
            print('Three',end=' ')
        elif i == '4':
            print('Four',end=' ')
        elif i == '5':
            print('Five',end=' ')
        elif i == '6':
            print('Six',end=' ')
        elif i == '7':
            print('Seven',end=' ')
        elif i == '8':
            print('Eight',end=' ')
        elif i == '9':
            print('Nine', end=' ')
        else:
            pass

    break
=============================================================================================
QUE 20 write a program to find power of number.
--------------------------------------------------------------
x1 = int(input('Enter the base of number'))
x2 = int(input('Enter the exponent of number'))
result = pow(x1, x2)
print('Answer = ', result)
--------------------------------------------------------------------------------------------------------------------------------
x = int(input('Enter a number: '))
y = int(input('Enter a power: '))
temp = 1
for i in range(y):
    temp = temp*x
print(temp)
=============================================================
QUE 21 write a program to find factorial of number.
---------------------------------------------------
from math import *
x1 = int(input('Enter the  number'))
print('The factorial of any number is',factorial(x1))
=============================================================

QUE 22 write a program to find HCF of two numbers
--------------------------------------------------

x1 = int(input('The First number is '))
y1 = int(input('The Second number is '))
def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
             hcf1 = i
    return hcf1
print('The HCF of two numbers',hcf(x1,y1))

===============================================
QUE 23 write a program to find LCM of two numbers
----------------------------------------------------

num1 = int(input('The First numn ber is '))
num2 = int(input('The Second number is '))
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)
print(max(num1, num2))
====================================================

QUE 24 write a program to check prime number.

num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
   ======================================================
QUE 25 write a program to find prime number from 1 to n.

min = int(input("Enter the min : "))
max = int(input("Enter the max : "))
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n, end = ' ')

Ans:
Enter the min : 20
Enter the max : 95
23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89
=============================================================================
QUE 26 write a program to add prime number from 1 to n.

upto = int(input("Find sum of prime numbers upto : "))

sum = 0

for num in range(2, upto + 1):

    i = 2

    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break;

    # If the number is prime then add it.
    if i is not num:
        sum += num

print("\nSum of all prime numbers upto", upto, ":", sum)
=========================================================================


QUE 27 write a program to check an armstrong numbers
-------------------------------------------------------
num = int(input('Enter a number: '))
num_original =num2=num
sum1 = 0
cnt=0

while(num>0):
	cnt=cnt+1
	num=num//10
while num2>0:
   rem = num2% 10
   sum1 += rem ** cnt
   num2//= 10

if(num_original==sum1):
    print('Armstrong!!')
else:
    print('Not Armstrong!')

=================================================================

QUE 28 write a program to check an armstrong numbers from 1 to n


print("Enter Range (Interval): ")
first = int(input())
last = int(input())

if first>last:
  temp = first
  first = last
  last = temp

while first<=last:
  res = 0
  temp = first
  noOfDigit = 0
  while temp>0:
    temp = int(temp/10)
    noOfDigit = noOfDigit + 1
  num = first
  while num>0:
    rem = num%10
    pow = 1
    i = 0
    while i<noOfDigit:
      pow = pow*rem
      i = i+1
    res = res+pow
    num = int(num/10)
  if res == first:
    print(res)
  first = first+1
===================================================================
QUE 29 write a program to check an armstrong numbers from 1 to n

Armstrong number: if the sum of its own digits raised
to the power number of digits gives the number itself.
--------------------------------------------------------------------
min = int(input('Enter the number To check whether armstrong '))
max = int(input('Enter the number To check whether armstrong '))
min1 = str(min)
maxx = str(max)
for j in range(min, (max + 1)):
    x2 = 0
    x3 = []
    x3.extend(str(j))
    p = len(x3)
    for n in x3:

        x2 += (int(n)**p)
# print(x2)
    if x2 == int(j):
        print(j, 'is an Armstrong number')

else:
    print('Range has no other Armstrong number')
--------------------------------------------------------------

x = int(input('Enter the number To check whether armstrong '))
x1 = str(x)
x2 = 0
x3 = []
x3.extend(x1)
p = len(x3)

for i in x3:
    x2 += int(i)**p
#print(x2)
if x2 % x == 0:
    print(x, 'is an Armstrong number')
else:
    print(x, 'is not an Armstrong number')

=============================================================

QUE 30 write a program to get star series


for i in range(1,6):
    print(i*"*")
 =============================================

QUE 31 write a program to get number series

def fibonacci(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(1, n-1):
            sequence.append(sequence[i-1] + sequence[i])
    return sequence
x = int(input('The fibonacci series is: '))
print(fibonacci(x))
------------------------------------------------------
n = int(input('The fibonacci series of count :'))
x = [0, 1]
for i in range(1,(n-1)):
    x.append(x[i]+x[(i-1)])
print(x)
======================================================================================================

n = int(input('Enter the number for summation'))
x = str(n)
s = []
sum1 = 0
while n > 0:

    for i in x:
        s.extend(i)
        sum1 += int(i)
    print(sum1)
    break
====================================================================
FIND  PRODUCT OF ALL DIGITS OF NUMBER
-----------------------------------------
n = int(input('Enter the number'))
x = str(n)
prod = 1

while n > 0:
    for i in x:
        prod *= int(i)
    print('The product of number is :', prod)
    break
==========================================================
QUE WAP on reverse of digits

n = input('Enter the string')
x = str(n)
s = []
while True:
    for i in x:
        s.extend(i)
    print(''.join(s[::-1]))
    break
==================================================
QUE WAP on factorial on num

from math import *
n = int(input('Enter the number'))

print(factorial(n))
--------------------------------------------------
x = int(input('Enter the number whose factorial is found out'))

for i in range(1,x):
    x *= i
print(x)

============================================
QUE left triangle pattern
-----------------------------------------------
for i in range(0,6):
    for j in range(5,i,-1):

        print('*', end = '')
    print()
=========================================================

WAP on swapcase of first and last digit of numbers
---------------------------------------------------------

n = int(input('Enter the number whose swaping is to be done'))
s = str(n)
print(l)
n=int(input('Enter the natural number'))
======================================================================='''
def obj(o):
    for i in o:
        if i==o[0]:
            print(o[-1])
        elif i==o[-1]:
            print(o[0])
 ṇ
















