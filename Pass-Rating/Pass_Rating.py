# pass rating converter

c = raw_input('Pass completions: ')     # pass completions
a = raw_input('Pass attempts: ')        # pass attempts
y = raw_input('Total passing yards: ')  # total passing yards
t = raw_input('Touchdowns: ')           # touchdowns
i = raw_input('Interceptions: ')        # interceptions

C = (((int(c) / int(a)) * 100) - 30) / 20
Y = ((int(y) / int(a)) - 3) / 4
T = (int(t) / int(a)) * 20
I = 2.375 - ((int(i) / int(a)) * 35)

rating = ((C + Y + T + I) / 6) * 100

quality = str()

if rating <= 85:
    quality = 'poor'
elif rating > 85 and rating <= 90:
    quality = 'mediocre'
elif rating > 90 and rating <= 95:
    quality = 'good'
else:
    quality = 'great'

print ('After much deliberation, we have determined that the pass rating is ' \
       + str("%.1f" % rating) + '.')
print ('This pass rating is ' + quality + '.')
