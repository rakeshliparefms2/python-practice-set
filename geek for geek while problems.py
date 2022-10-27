'''Write a Python function to check whether a number falls in a given range

n = [5,25,68,23,57,89,888,45]
n1 = int(input("Enter the number to find out"))
for i in n:
    if i == n1:
        print('The num',i,'present in the list')
        break
else:
    print('The number is not present')
---------------------------------------------------------
n = [5,25,68,23,57,89,888,45]
n1 = int(input("Enter the number to find out"))
if n1 in n:
    print('The num',n1,'present in the list')
else:
    print('The number is not present')
==================================================================================================
 QUE 2 . Write a Python function that accepts a string and
 calculate the number of upper case letters and lower case letters.

s = 'iojoijllkLKLKK'
d={"UPPER_CASE":0, "LOWER_CASE":0}
for c in s:
    if c.isupper():
        d["UPPER_CASE"]+=1
    elif c.islower():
        d["LOWER_CASE"]+=1
    else:
        pass
print ("Original String : ", s)
print ("No. of Upper case characters : ", d["UPPER_CASE"])
print ("No. of Lower case Characters : ", d["LOWER_CASE"])

s = 'iojoijllkLKLKK1235'
c = {'upper1': 0,'lower1': 0}
for p in s:
    if p.isupper():
        c['upper1'] += 1
    elif p.islower():
        c['lower1'] += 1
    else:
        pass
print('Original string',s)
print('No. of upper case letters : ', c['upper1'])
print('No. of upper case letters : ', c['lower1'])
===================================================================================
QUE 3.  Write a Python function that takes a number as a parameter and check the number is prime or not.
---------------------------------------------------------------------------------------------------------

#def prime(n1):
n = int(input('Enter the number to check prime or not'))
def prime(n1):
    if n > 1:
        for x in range(2,n):
            if (n % x) == 0:
                print(n, 'is not prime num')
                break
        else:
            print(n,'is a prime number')
    else:
        print('not a prime number')
prime(n)
================================================================================
QUE 4: Write a Python program to print the even numbers from a given list.
------------------------------------------------------------------------------

ls = [1, 3, 5, 64, 55, 88, 885, 99, 44, 78, 99, 100 ]
le = []
def even(l):

    for i in ls:
        if i % 2 == 0:
            le.append(i)
    print('The list of even numbers is:', le)
even(ls)
==========================================================================

QUE 5 WAP to check string is palindrome
----------------------------------------------------------

s = str(input('Enter the string to check palindrome'))
l = len(s)
x = l / 2

def pd(p):

    if l % 2 == 0:
        if s[:] == s[::-1]:
            print('The string is palindrome')
        else:
            print('The string is not palindrome')
    elif l % 2 != 0:
        if s[:] == s[::-1]:
            print('The string is palindrome')
        else:
            print('The string is not palindrome')
    else:
        pass
pd(s)
======================================================================================
QUE 6. Write a Python function to check whether a number is perfect or not
--------------------------------------------------------------------------------

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(256))
===================================================================================
QUE 7.Write a Python function that prints out the first n rows of Pascal's triangle
----------------------------------------------------------------------------------
'''




















