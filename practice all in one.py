'''def string(str1):
    count = 0
    for i in str1:
        count += 1
    return count
s = string('Write a Python program to calculate the length of a string.')
print(string('Write a Python program to calculate the length of a string.'))
=============================================================================
Q 2 write python function to multiply all elements in a list

def ls(value):
    prod = 1
    for i in value:
        prod *= i
    return prod
print(ls((2, 5, 6, 7, -3, 4)))
====================================================================
Q 3. WAP to sort second element of list of tuple in ascending order
---------------------------------------------------------------------

l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
l.sort(key = lambda x:x[1])
print(l)
print(dict(l))
print(list(dict(l)))
print(list(dict(l).values))

------------------------------------------------------------------------
=============================================================================
Q 4. WAP for checking list empty.
-----------------------------------

l = [1, 2]
if not l:
    print('List is empty')
else:
    print('List is not empty')
==============================================================================
Q 5 . WAP on dictionary to sort by value
-------------------------------------------







=======================================================================================
Q 6. WAP string whose second occurance of letter is change to $
-----------------------------------------------------------------
s = str(input('Enter the string whose second occurance of letter is change to $'))
x = s[0]
x1 = list(s[1:].split())
x2 = ''.join(x1)
print(x2)
if x in x2:
    p = x2.replace(x,'$')
print(x+p)
=====================================================================================
Q 7. Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
--------------------------------------------------------------------------------------

s = str(input('Enter the string to change it in "ing" or "ly"'))
s1 = len(s)
if len(s) >= 3:
    if s[-3:] != 'ing':
        print(s+'ing')

    else:
        print(s+'ly')
else:
    print(s)
===================================================================================
Q 8. Write a Python program to find the list of words that are
longer than n from a given list of words.
------------------------------------------------------------------

s = str(input('Enter the string'))
ls = []
s1 = s.split()
for i in s1:
    if len(i) >= 4:
        ls.append(i)
print(ls)
=========================================================================================
Q 9. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
-----------------------------------------------------------------------------------------------------

list1 =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
unwanted = [0,2,5]

for ele in sorted(unwanted, reverse=True):
    del list1[ele]

print(list1)
=============================================================================================================
Q 10. Write a Python script to sort (ascending and descending) a dictionary by value.

def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
print("Original dictionary elements:")
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
print(colors)
print("\nSort (ascending) the said dictionary elements by value:")
print(sort_dict_by_value(colors))
print("\nSort (descending) the said dictionary elements by value:")
print(sort_dict_by_value(colors, True))
===========================================================================================
Q 11.  Write a Python script to add a key to a dictionary
------------------------------------------------------------------------------------------
d = {1: 'apple', 2: 'mango', 3: 'peer'}

d.setdefault(4, 'banana')
print(d)
==========================================================================
Q 12. write script to add all dictionary.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic = {}
dic.update(dic1)
dic.update(dic2)
dic.update(dic3)
print(dic)
====================================================================
Q 13 write a program to find LCM of two numbers
-------------------------------------------------------------------

num1 = int(input('Enter the number'))
num2 = int(input('Enter the number'))
for i in range(max(num1,num2),(1+(num1*num2))):
    i % num1 == i % num2 == 0
print(i)
===========================================================================
Q 14. create dict of {x:x*x} type
---------------------------------------------------------------------------

n = int(input('Enter the number '))
x = dict()
for i in range(1,n+1):
   x[i] = i*i
print(x)
==========================================================================
Q 15. Create dict of product of values  type
---------------------------------------------------------------------------

d = {'a':2, 'b':44, 'c':-33, 'd':88}
prod = 1
for i in d:
    prod *= d[i]
print(prod)
======================================================================================
Q 16. 
--------------------------------------------------------------------------------------


n1 = int(input('Enter the first num'))
n2 = int(input('Enter the first num'))
if n1 > n2:
    print('The first number',n1, ' is greater than ',n2)
else:
    print('The second number', n2, 'is greater than', n1)

n1 = int(input('Enter the first num'))
n2 = int(input('Enter the second  num'))
n3 = int(input('Enter the third num'))
if n1 > n2 and n1 > n3:
    print('The First number',n1, ' is greater than ',n2,'&' ,n3)
elif n2 > n1 and n2 > n3:
    print('The Second number',n2, ' is greater than ',n1,'&' ,n3)
else:
    print('The Third number', n3, ' is greater than ', n2, '&', n1)

yr = int(input('Enter the year'))
if yr % 100 == 0:
    if yr % 400 == 0:
        print('The year', yr, 'is leap year')
    else:
        print('The year', yr, 'is not leap year')
else:
    if yr % 4 == 0:
        print('The year', yr, 'is leap year')
    else:
        print('The year', yr, 'is not a leap year')


s = int(input('Enter the amount of Rupees \nto count the no. of notes'))
if s % 2000 == 0:
    print('The total number of Rs.2000 notes are', s / 2000)
else:
    print('The number of Rs.2000 notes count with remainder', s // 2000)
x = s - (s // 2000 * 2000)
if x % 500 == 0:
    print('The total number of Rs.500 notes are', x / 500)
else:
    print('The number of Rs.500 notes count with remainder', x // 500)
x1 = x - (x // 500 * 500)
if x1 % 200 == 0:
    print('The total number of Rs.200 notes are', x1 / 200)
else:
    print('The number of Rs.200 notes count with remainder', x1 // 200)
x2 = x1 - (x1 // 200 * 200)
if x2 % 100 == 0:
    print('The total number of Rs. 100 notes are', x2 / 100)
else:
    print('The number of Rs.100 notes count with remainder', x2 // 100)
x3 = x2 - (x2 // 100 * 100)
if x3 % 50 == 0:
    print('The total number of Rs.50 notes are', x3 / 50)
else:
    print('The number of Rs.50 notes count with remainder', x3 // 50)
x4 = x3 - (x3 // 50 * 50)
if x4 % 20 == 0:
    print('The total number of Rs.20 notes are', x4 / 20)
else:
    print('The number of Rs.20 notes count with remainder', x4 // 20)
x5 = x4 - (x4 // 20 * 20)
if x5 % 10 == 0:
    print('The total number of Rs.10 notes are', x5 / 10)
else:
    print('The number of Rs.10 notes count with remainder', x5 // 10)
x6 = x5 - (x5 // 10 * 10)
if x6 % 5 == 0:
    print('The total number of Rs.5 notes are', x6 / 5)
else:
    print('The number of Rs. 5 notes count with remainder', x6 // 5)
x7 = x6 - (x6 // 5 * 5)
if x7 % 2 ==0:
    print('The total number of Rs.2 notes are', x7 / 2)
else:
    print('The number of Rs.2 notes count with remainder', x7 // 2)
x8 = x7 - (x7 // 2 * 2)
if x8 % 1 == 0:
    print('The total number of Rs.1 notes are', x8 / 1)
else:
    print('The number of Rs. 1 notes count with remainder', x8 // 1)





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
-------------------------------------------------------------------
n = int(input('Enter the natural num till which we want series'))
ls = []
for i in range(1,n+1):
    print (i, end = ' ')
--------------------------------------

for i in range(65,91):
    print(chr(i),end = ' ')
for i in range(97,123):
    print(chr(i),end = ' ')
-------------------------------------
n = int(input('Enter the natural num till which we want series'))
add1 = 0
for i in range(1,n+1):
    add1 += i
print (add1, end = ' ')
-----------------------------------------------
n = int(input('Enter the natural num till which we want series'))
add1 = 0
for i in range(1,n+1,2):
    add1 += i
print (add1, end = ' ')
-----------------------------------------------
n = int(input('Enter the number whose table is to be formed'))

for i in range(1,11):
    mul = n*i
    print(n, 'X', i,' =', mul)
---------------------------------------------------------------------
x = str(input('Enter the string and check whether it is alphabet'))
vowel = ['a','e', 'i','o','u']
for i in x:
    if i.isalpha():
        if i in vowel:
            print(i,': alphabet which is vowel')
        else:
            print(i,': alphabet which is consonant')
    else:
        print(i,': not alphabet')

---------------------------------------------------------------
for i in n:
    if i.isalpha():

        if i.islower():
            print(i, ': lowercase alphabet')
        else:
            print(i, ': Uppercase alphabet')
    else:
        print(i,': not an alphabet')
-------------------------------------------------------
def val(n1,n2):
    if n1> n2:
        return n1
    else:
        return n2
x1 = int(input('Enter the num1'))
x2 = int(input('Enter the num2'))
p = val(x1,x2)
print(p)

------------------------------------------------------------------------------
s = 'Rakesh Lipare'
for i in range(len(s)-1,-1,-1):
print(s[i], end = '')

-------------------------------------------------------------------------------
m = 'Manisha Lipare'
r = ''
for i in m:
    r = i+r
print(r)

=========================
IMP    PYTHON PROGRAM APP
=========================
x = int(input('Enter the number '))
if x <= 17:
    print('The Difference is :', 17-x)
else:
    print('The value is:',(x-17)*2)
----------------------------------------------------
#ONE LINER SOLUTION
res = lambda x: (17-x) if x<=17 else (x-17)*2
print(res(25))
----------------------------------------------------
def s1(x):
    if x<=17:
        return 17-x
    else:
        return(x-17)*2
print(s1(23))
print(s1(12))
======================================================
x=int(input('Enter the number'))
y=int(input('Enter the number'))
z=int(input('Enter the number'))
if x==y==z:
    print((x+y+z)*3)
else:
    print(x+y+z)
----------------------------------------
def s1(x,y,z):
    if x==z==y:
        return (x+z+y)*3
    else:
        return x+z+y
print(s1(10,20,30))
print(s1(20,20,20))
--------------------------------------------------
res = lambda x,y,z: (x+y+z)*3 if x==y==z else (x+y+z)
print(res(20,30,20))
====================================================================
$$$$$ ONE LINER SOLUTION
str1 = lambda str2,n: str2*n
print(str1(str2 = 'Rakesh', n = 10))
------------------------------------------
str1 = input("enter the string")
n = int(input('Enter the integer'))
for i in range(n):
    print(str1,end=' ')
-------------------------------------------
def str(s,n):
    for i in range(n):
        return s*n
print(str('try',100))
=============================================
To find largest number in list
------------------------------
a = []
n = int(input('Enter the number of elements in list'))
for i in range(n):
    b = int(input('Enter the element'))

a.append(b)
a.sort(reverse=True)
print('The largest number is',a[0])
--------------------------------------
def ls(list):
   list.sort(reverse = True)
   return list[0]
print(ls([5,6,9,8,3]))
---------------------------------------------------
from functools import reduce
k = [34,56,12,23,567,333,99,455]
res = reduce(lambda x,y: x if x>y else y,k )
print(res)
==============================================================
lists of even num and odd nums
--------------------------------
ls = [2,5,6,8,9,65,84,55,21,27,59,28,36,49]
ls1 = []
ls2 = []
for i in ls:
    if i%2==0:
        ls1.append(i)
    else:
        ls2.append(i)
print('The even num list', ls1)
print('The even num list',ls2)
---------------------------------------------------------------------
ls1 = []
ls2 = []
def num(list):
    for i in list:
        if i%2==0:
            ls1.append(i)
        else:
            ls2.append(i)
    return ls1, ls2
print(num([2,5,6,8,9,65,84,55,21,27,59,28,36]))
------------------------------------------------------
ls = [2,5,6,8,9,65,84,55,21,27,59,28,36]
even_num = list(filter(lambda x: x %2==0, ls))
odd_num  = list(filter(lambda x: x %2==1, ls))
print('The even numbers in list are:', even_num,'The odd numbers in list are :',odd_num)
============================================================================================
MERGE TWO LISTS AND SORT IT
--------------------------------
ls1 = [56,41,87,35,46,97,12,9]
ls2 = [99,47,95,351,47,118,66,23]

ls = ls1 + ls2
l = set(ls)
l1 = list(l)
l2 = l1.sort()
print(l1)
========================================================================
$$$$$$$$$$    STRING PROBLEMS   $$$$$$$$$
remove the nth index  letter from a string
------------------------------------------
s = 'The basic concept of programming is logic and is build by practicing'
n = int(input('Enter the index of string to be removed'))
for i in range(len(s)):
    if i == n:
        continue
    print(s[i],end='')
-------------------------------------------------------------------------------
def str(s,n):
    for i in range(len(s)):
        if i == n:
            continue
    return s[:n]+s[n+1:]
n1 = int(input('Enter the index of string to be removed'))
st = 'The basic concept of programming is logic and is build by practicing'
print(str(st,n1))
------------------------------------------------------------------------------
==============================================================================
ls =  [1,2,3,4,5]
print(list(map(lambda x:x**2,ls )))
print(list(map(lambda x:x**3,ls )))
------------------------------------
Write a Python program to get a list, sorted in increasing order by the last element
in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#def last(n):
 #   return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=tuples[-1])

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
l.sort(key = lambda x:x[1])
print(l)
print(dict(l))
print(list(dict(l)))
print(list(dict(l).values))
===========================================================================================
program to replace 'a' to '$'in a string
s = 'Fruits Apple Orange Guava Mango '
s =s.replace('a','$')
s = s.replace('A','$')
print(s)
-----------------------------------------------

s = 'Fruits Apple Orange Guava Mango '
for i in s:
    if i =="a" or i =="A":

        print('$',end='')
    else:
        print(i,end='')
---------------------------------------------------------
s = 'Fruits Apple Orange Guava Mango '
print(list(map(lambda x: '$' if x=='a' or x=='A' else x,s)))
x = list(map(lambda x: '$' if x=='a' or x=='A' else x,s))
print("".join(x))
------------------------------------------------------------------
TO EXCHANGE LAST AND FIRST DIGIT  OF STRING


s = 'Fruits Apple Orange Guava Mango'
print(s[-1:]+s[1:-1]+s[0])
--------------------------------------------
s = 'Fruits Apple Orange Guava Mango'
st = list(s)
print(st)
hold = st[0]
st[0]=st[-1]
st[-1]= hold
print(''.join(st),end='')
==================================================
Que. PRINT NUMBER OF VOWELS IN STRING
s = 'Fruits Apple Orange Guava Mango'
v ='aeiouAIEOU'
count = 0
for i in s:
    if i in v:
        count += 1

print(count)
-----------------------------------------------------
----------------------------------------------------------------------------------------------
PATTERN PROBLEMS
============================
for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()
Ans:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
===============================================
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
=============================================================

for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()
Ans:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
===========================================================
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end= ' ')
    print()

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
===========================================
for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=' ')
    print()

1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
============================================
for i in range(5,0,-1):
    for j in range(0,i):
        print(5,end=' ')
    print()

5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
=============================================================

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=' ')
    print()
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
=======================================================
for i in range(4,0,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print()

0 1 2 3 4
0 1 2 3
0 1 2
0 1
====================================================
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

for i in range(1,9):
    for j in range(i-1,-1,-1):

        print(2**j,end=' ')
    print()

1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
64 32 16 8 4 2 1
128 64 32 16 8 4 2 1
=======================================================================
QUE: In series find no. of even and odd numbers

ls = [5,7,8,4,77,99,55,222,666,88,78,9,90]
count_even=0
count_odd =0
for i in ls:
    if i%2 == 0:
        count_even += 1

    else:
        count_odd += 1
print('The Even number is',count_even)
print('The Odd numbers are:',count_odd)
==================================================================================

QUE: p+q+r+s=n where n<=4000,p,q,r,s =0-1000


n = int(input('The number to be entered'))
count = 0
for p in range(1,11):
    for q in range(1,11):
        for r in range(1,11):
            for s in range(1,11):
                if p+q+r+s == n:
                    count +=1

                else:
                    pass
print(count)
-===================================================================================
QUE: count num of elements within specified range

n1 = int(input('Enter the first number ' ))
n2 = int(input('Enter the Second number'))
ls = [12,23,25,87,45,59,84,92,64,67,29,37,29,66,55,451,93,944]
count = 0
for i in ls:
    if i in range(n1,n2+1):
        count+=1
print('The count of numbers in between ',n1,'and ',n2,'is:',count)
---------------------------------------------------------------------
def num(n1,n2,n):
    count = 0
    for i in n:

        if i in range(n1,n2):
            count += 1
    return count
nx = [12,23,25,87,45,59,84,92,64,67,29,37,29,66,55,451,93,944]
n_1 = int(input('Enter the first number ' ))
n_2 = int(input('Enter the Second number'))
print(num(n_1,n_2,nx))
--------------------------------------------------------------------
n1 = int(input('Enter the first number ' ))
n2 = int(input('Enter the Second number'))
ls = [12,23,25,87,45,59,84,92,64,67,29,37,29,66,55,451,93,944]
ls1 =[]
x = [ls1.append(i) for i in ls if i in range(n1,n2+1)]
print(len(ls1))
===========================================================================================
QUE: convert tis string  green-blue-black-red-orange-yellow-violet-white to black-blue-green-ornge-red-violet-white-yellow

s = 'green-blue-black-red-orange-yellow-violet-white'

ls = s.split('-')
ls.sort()
print('-'.join(ls))
========================================================================================
QUE: square of odd numbers in list by list comprehension

ls =[23,4,5,6,7,8,9,1,3,44,33,66,77,88,99,101,333,555,777,85,-3,-4,-8]
x = [i**2 for i in ls if i%2!=0 and i>0]
print(x)
---------------------------------------------------------------------------------------

'''
































































































































































































































































































































































































































































 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































