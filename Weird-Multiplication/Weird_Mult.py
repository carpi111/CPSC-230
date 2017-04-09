# Russian Peasant/Ancient Egyptian multiplication

a = raw_input('What is the first integer? ')
b = raw_input('What is the second integer? ')

negative1 = bool
negative2 = bool

# if user inputs letters instead of numbers
if a.isalpha() is True or b.isalpha() is True:
    print ('')
    print ('Only use numbers.')
    exit()

a = int(a)
b = int(b)

# if first number is negative
if a < 0 < b:
    negative1 = True
# if second number is negative
elif b < 0 < a:
    negative2 = True
# if both are positive or if both are negative
else:
    negative1 = False
    negative2 = False

a = abs(a)
b = abs(b)

product = 0

# while "b" is greater than 0
while b != 0:
    # if "b" is odd
    if b % 2 != 0:
        product = product + a
        a *= 2
        b //= 2
    # if "b" is even
    if b % 2 == 0:
        a *= 2
        b //= 2

# if either number is negative (but not both) multiply the answer by -1
if negative1 is True:
    product *= (-1)
elif negative2 is True:
    product *= (-1)

print ('')
print ('The product is ' + str(product) + '.')
