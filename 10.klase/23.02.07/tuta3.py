"""#Ģenerējiet veselus skaitļus no 0 līdz 6

for i in range (7):
    print(i)
 

# Kāda būs x vērtība pēc koda izpildes
x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

while (x<100):
    x+=2
print(x)


# Kāda būs x vērtība pēc koda izpildes
a, b = 12, 5

if a + b:
    print('True')
else:
    print('False')


#Kāda būs x vērtība pēc koda izpildes
for num in range(-2,-5,-1):
    print(num, end=", ")
"""

# Kāda būs x vērtības pēc koda izpildes
x=0
for i in range(10):
    for j in range(-1,-10,-1):#ligzdots cikls (cikls ciklā)
        x+=1
        print(x)

"""
i   j   x
        0
0  -1   1
   -2   2
   -3   3
   -4   4
   -5   5
   -6   6
   -7   7
   -8   8
   -9   9
   -10  10
1  -1   11
   -2   12
   -3   13
   -4   14
   .....
   -10  20
2  -1   21
   -2   22
   .....
...........

"""