#Home Work 2
#Task 1
age1 = float (input('Введите ваш возраст:'))
y = age1
if y < 18:
    print('Извините, пользоваться данным ресурсом можно только с 18 лет')
else:
    print('Доступ разрешен')
#Task 2
my_list = range(0, 21)
answer = input('Четные или нечетные?:')
for it in my_list:
    if answer == 'четные':
        print(int (it % 2 == 0))
    else:
        answer == 'нечетные'
        print(int (it % 2 == 1))
#Task 3
num = input('Введите ваше число:')
num = int (num)
while num > 0:
    ostatok = num % 10
    num //=10
    print(ostatok, num)