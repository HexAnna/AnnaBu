#Home Work 3
#Task 1
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
fruts_list = ['Яблоки', 'Апельсины', 'Груши', 'Черешня', 'Авокадо', 'Дыня']
for i in range(len(fruts_list)):
    print(str(i+1) + '. ' + "{:>10}".format(str(fruts_list[i])))

#Task 2
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
lst1 = [1, 5, 8, 10, 12, 15]
lst2 = [3, 18, 9, 5]
res = []
print(lst1, lst2)
for i in lst1:
    if i not in lst2:
        res.append(i)
lst1 = res
print(lst1, lst2)
print()

#Task 3
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

w = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]
t = []
print(w)
for i in w:
    if i % 2 == 0:
        t.append(int(i / 4))
    else:
        t.append(i * 2)
print(t)
