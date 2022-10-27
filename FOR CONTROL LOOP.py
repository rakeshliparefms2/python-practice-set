########   ans: BACHCHAN AMITABH
'''s = 'Amitabh Bachchan'
for i in s.split()[::-1]:
    print(i,end=' ')
######### Ans : nahchcaB hbatimA
s = 'Amitabh Bachchan'
print(s[::-1])
##Ans : nahchcaB hbatimA
s = 'Amitabh Bachchan'
#print(reversed(s))
print(tuple(reversed(s)))
final = ''
for i in reversed(s):
    final += i
    print(final)

##Ans : nahchcaB hbatimA
s = 'Amitabh Bachchan'
for i in range(-1,-(len(s)+1),-1):
    print(s[i], end = '')
    ==================================
## ANS: hbatimA nahchcaB
s = 'Amitabh Bachchan'
for i in s.split():
    print(i[::-1], end = ' ')
==================================
# find vowels in s = 'Amitabh Bachchan'
s = 'Amitabh Bachchan'
vowels = ['a','i','o','u','e','A','I','O','U','E']
for i in s:
    if i in vowels:
       print(i, end=' ')
   ====================================
# TO FIND {A:1, a:3, m:1,.......}
s = 'Amitabh Bachchan'
d = {}
for i in s:
    #print(i,s.count(i))
     d[i]=s.count(i)
     print(d)
     =======================================================
############# ANS: HANTABH BACHAMI
s = 'Amitabh Bachchan'
s_1 = list (s)
s_2 = int(len(s))
for i in s_1:
    s_1[0] = s_1[s_2 - 3]
    s_1[1] = s_1[s_2 - 2]
    s_1[2] = s_1[s_2 - 1]
s_1[s_2 - 3] = s[0]
s_1[s_2 - 2] = s[1]
s_1[s_2 - 1] = s[2]
d = ''.join(s_1)
print(d)
==============================================================
for: Amitabh Bachchan
Get: Dplwdek Edfkfkdq
------------------------
s = 'Amitabh Bachchan'
for i in s:
    if(i.isalpha()):
        print(chr(ord(i)+3), end = '')
    else:
        print(' ', end = '')
=======================================================
#############   current character A position at 0          ##########
s = 'Amitabh Bachchan'
for index, char in enumerate (s):
    print('current character', char,'position at', index)
====================='''
