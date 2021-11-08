#HomeWork 4
#Task 1
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

km = float(input('Киллометры:'))
p = km * 1.609
print('Miles:', p)

def mile(x): 
        return 1.609 * x
def main():
    for n in range(100,100,1501):
        print(n,miles(n))
#Task 2
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

import math
def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    mul =  number*degree
    res = int(mul)
    ost = mul-res
    # print(number,mul,res,ost)
    if not (abs(ost) < 0.5):
        if res>0: res+=1
        else: res-=1
    return res/degree

my_round(2.1234567, 5)
    return sum(a[:b]) == sum(a[b:])

# Task 3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    tn_list=str(ticket_number)
    if len(tn_list) != 6: return False
    first=0
    last=0
    for i in range(3):
        first+=int(tn_list[i])
        last+=int(tn_list[-i-1])
    return first==last

def test(got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Получено: {1} | Ожидалось: {2}".format(prefix, repr(got), repr(expected)))

print("Задача 1. Округление.")
test(my_round(5.234,2),5.23)
test(my_round(5.255,2),5.26)
test(my_round(-5.245,1),-5.2)
test(my_round(-5.255,1),-5.3)

print("\nЗадача 2. Билет.")
test(lucky_ticket(345534),True)
test(lucky_ticket("045414"),True)
test(lucky_ticket(345043),False)
test(lucky_ticket(345542),False)
