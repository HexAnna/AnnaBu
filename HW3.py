#HomeWork 3
#Task 1
km = float(input('Киллометры:'))
p = km * 1.609
print('Miles:', p)
#Task 2
import math
q = float(input('Your number:'))
p = round (q, 5)
print(p)
#Task 3
s = int (input('Your ticket number: '))
def lucky_ticket (s):
    a = [int(i) for i in s]
    return sum (a[:3] == sum (a[3:]))
