
# Ques1)-
import string


a = 'Hii this is python programming '
print(type(a))
print(id(a))


# Ques 2)-
var = 'This is python class'
print(var)

print("This is python class")

print('''This is python class''')

print("""This is python class""")

print('This is python class')

# print('This is python's class')            # invalid

# print("learnbay provide "java", "python" classes")      # ---> invalid

print("learnbay provides 'java','python' classes")

print("This is python's class")

print("""learnbay provide "java", "python" classes""")

print('''Learnbay provide "java", "python" classes''')

print('''Learnbay provides 
"java", "python" 
classes''')

# print('This is 
# python 
# class')            # ---> invalid

#  Ques 3)- 
my_str = "Although that way may not be obvious at first unless you're Dutch."
my_str1 = "Although that way may not be obvious at first unless you're Dutch."
s = len(my_str)
print(f'the lenght of my_str is:',s)

print(id(my_str),id(my_str1))
print(f'the id of my_str and my_str1 is :',(id(my_str) is id(my_str1)))

print(f'Type of my_str is:',type(my_str))


# Ques 4)- 
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
print(f'the first character of my_str is:', my_str[0])

print(len(my_str))
print(f'the first character in my_str is:', my_str[7])

print(f'the character at index at 10 in my_str is: ', my_str[10])

print(f'the last character in my_str is: ',my_str[-1])

print(f'the last character in my_str is: ',my_str[7])

print(f'the character in my_str is: ',my_str[9])




#   Ques 5)- 
my_str = "Although that way may not be obvious at first unless you're Dutch."

print(f'you have sliced : ',my_str[::])
print(f'you have sliced : ',my_str[0:len(my_str):])
print(f'you have sliced :',my_str[::-1])
print(f'you have sliced :',my_str[5:20:3])
print(f'you have sliced :', my_str[8:9:-57])
print(f'you have sliced :', my_str[::2])
print(f'you have sliced :', my_str[::3])
print(f'you have sliced :', my_str[::-1])
print(f'you have sliced :', my_str[66::-1])
print(f'you have sliced :', my_str[::-2])
print(f'you have sliced :', my_str[66:0:-2])
print(f'you have sliced :', my_str[10:17:-1])
print(f'you have sliced :', my_str[16:10:-1])
print(f'you have sliced :', my_str[49:56:1])
print(my_str.index('ess',0,66))
print(len(my_str))

# Ques 6)-
str1 = 'Learnbay'
str2 = 'Python'
print(str1+' '+str2)

# type error : can only concatenate str(not int) to str
# int1 = 20
# str = 'python'
# print(int1+str)

# type error : can only concatenate str(not float) to str
# float = 45.20
# str = 'python'
# print(float+str)

print(str1*3)

# type error: can't multiply sequence by non interger type float
# str1 = 'python'
# float = 45.30
# print(str1*float)


# type error: can't multiply senquence by non integer type 'str'
# str2 = 'python'
# non_int = '345.34'
# print(str2*non_int)


#   Ques 7)-
str1 = 'Python'
str2 = 'Python'
str3 = 'Python$'
str4 = 'Python$'
print(str1 is str2)
print(str1 is str3)
print(str4 is str3)

# true and false by using membership operator #
print('P' in str1)
print('$'in str3)
print('N' in str3)


# Ques 8)-
str1 = 'This is python class'
print(str1.replace('python','java'))
# str1[3] = 'A'
# print(str1)



# Ques 9)-
str1 = 'A'
str2 = 'A'
# print(str1 <= str2)
# print(str1 == str2)
# print(str1 != str2)
# print(str1 < str2)


# Ques 10)-
str1 = 'A'
str2 = 'a'
# print(str1 < str2)
# print(str1 != str2)
# print(str1 == str2)
# print(str1 > str2)


# Ques 11)-
str1 = 'A'
str2 = 65
# print(str1 >= str2)
# print(str1 != str2)
# print(str1 == str2)


# Ques 12)-
str1 = 'Python'
str2 = 'Python'

# print(str1 <= str2)
# print(str1 == str2)
# print(str1 != str2)
# print(str1 > str2)


# Ques 13)-
str1 = 'Python'
str2 = 'python'
# print(str1 <= str2 )
# print(str1 != str2 )
# print(str1 == str2 )
# print(str1 >= str2 )


# Ques 14)-
a = 'python'
b = ''
# print(a and b)
# print(a or b)
# print(a, not b)
# print(b and a)
# print(b or a)
# print(b, not a)


# Ques 15)-
a = ''
b = ''
# print(a and b)
# print(a or b)
# print(a, not b)


# Ques 16)-
a = 'Python'
b = 'learnbay'
# print(a and b)
# print(a or b)
# print(a, not b)



# Ques 17)- 
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
# print(my_str.find('t'))
# print(my_str.count('t'))
# print(my_str.index('t'))
# print(my_str.find('8'))
# print(my_str.index('8'))
# print(my_str.find('the'))
# print(my_str.index('the'))
# print(my_str.find('t',9,15))
# print(my_str.rfind('u'))
# print(my_str.rindex('u'))


# Ques 18)-
# a = '  python   '
# print(a.strip())

# b = '  python'
# print(b.lstrip())

# c = 'python   '
# print(c.rstrip())



# #   Ques 19)-
# my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

# print(my_str.upper())
# print(my_str.lower())

# my_str = "Although 8 ThAt way MaY not be ObviouS at FirSt unless you'Re DutCH"
# print(my_str.swapcase())



# # Ques 20)-
# in_str = input('Enter your line users: ')
# print(in_str.upper() )
# print(in_str.title())
# if in_str.upper():
#     print(in_str.title())
# if in_str.lower():
#     print(in_str.upper())
# else:
#     print('none')



# Ques 21)-
# a = 'py56thon'
# print(a.isalnum())
# b = 'python'
# print(b.isalpha())
# print(b.isalnum())


c = '34567'
# print(c.isdigit())
# print(b.isdigit())
# print(c.isnumeric())
# print(c.isdecimal())
# print(a.isdecimal())

d = 'PytHon'
# print(d.isupper())

# e = 'python'
# print(e.islower())

# f = 'PYTHON'
# print(f.isupper())
# print(f.islower())

# g = 'This Is Suman Sourabh'
# print(d.istitle())
# print(g.istitle())
# print(g.isspace())

# h = '   '
# print(h.isspace())



# s = 234.800
# x = 345
# # print(s.isdecimal)
# print(x.isdecimal)


#  Ques 22)-

z = input('Enter the line of string :')

if z is in 


