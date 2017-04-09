# Fahrenheit <-> Celsius Converter

x = raw_input('What is the known value?\n\n1. Fahrenheit  2. Celsius\n\n')

# degrees F to degrees C
if x == '1':
    print ('')
    f = input('How many degrees Fahrenheit? ')
    print ('')
    calc1 = ((float(f) - 32) * (5.0 / 9.0))
    calc1 = "%.2f" % calc1
    print (str(f) + ' F is ' + calc1 + ' C.')

# degrees C to degrees F
elif x == '2':
    print ('')
    c = input('How many degrees Celsius? ')
    print ('')
    calc2 = ((float(c) * 1.8) + 32.0)
    calc2 = "%.2f" % calc2
    print (str(c) + ' C is ' + str(calc2) + ' F.')
