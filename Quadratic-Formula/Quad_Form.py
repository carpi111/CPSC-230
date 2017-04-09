# Quadratic formula

import math

print ('F(X) = AX^2 + BX + C')
print ('')

a = input('What is A? ')
b = input('What is B? ')
c = input('What is C? ')

a = float(a)
b = float(b)
c = float(c)

# discriminant
d = (b**2) - (4*a*c)

if d < 0:
    print ('')
    print ('This equation has no solutions.')

elif d == 0:
    root1 = ((-b + (math.sqrt(d)))/(2*a))
    print ('')
    print ('The root is ' + str(root1) + '.')

else:
    root1 = ((-b + (math.sqrt(d)))/(2*a))
    root2 = ((-b - (math.sqrt(d)))/(2*a))

    # cuts down float to 5 decimal places
    root1 = "%.5f" % root1
    root2 = "%.5f" % root2

    print ('')
    print ('The roots are ' + str(root1) + ' and ' + str(root2) + '.')
