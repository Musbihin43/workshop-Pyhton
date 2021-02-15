# this is the first comment
spam = 1 # and this is  the second comment
        # ... and now a third!
text = "# this is not a comment because it's inside quotes"
print("-------------------------")
#-------------------------------
print ("perhitungan dasar")
print (2 + 2)
print ((50 - 5*6) / 4)
print (8 / 5)
print("-------------------------")
#-------------------------------
print ("pembagian dan sisa hasil bagi")
print (17/3)
print (17//3)
print (17%3)
print (5*3+2)
print("-------------------------")
#-------------------------------
print ("pangkat")
print (5**2)
print (2**7)
print("-------------------------")
#-------------------------------
width = 20
height = 5*9
print (width*height)
# n
print("-------------------------")
print (4*3.75-1)
print("-------------------------")
tax = 12.5/100
price = 100.50
result1 = price*tax
print(result1)
result2=price+result1
print(result2)
print(round(result2,2))
print("-------------------------")
print("-------------------------")
print("STRING")
'spam eggs'
'doesn\'t'
'"yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

print("-------------------------")

print('C:\some\name')
print(r'C:\some\name')
print("-------------------------")
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print("-------------------------")
# 3 times 'un', followed by 'ium'
print(3*'un'+'ium')
print("-------------------------")

print('py' 'thon')
print("-------------------------")

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print("-------------------------")

prefix ='py'
hasil = prefix + 'thon'
print(hasil)
print("-------------------------")

word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])
print("-------------------------")

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print (squares + [36, 49, 64, 81, 100])
print("-------------------------")

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
cubes.append(216)
cubes.append(7**3)
print(cubes)
print("-------------------------")

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
        print(a)
        a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
    
