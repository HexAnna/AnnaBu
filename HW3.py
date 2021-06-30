#Home Work 3
#Task 1
# Сначала так сделала
# fruts_list = ['Бананы', 'Яблоки', 'Груши', 'Черешня', 'Апельсины']
# print(
#     f"{'1. Бананы:':>15}",
#     f"\n{'2. Яблоки:':>15}",
#     f"\n{'3. Груша:':>15}",
#     f"\n{'4. Черешня:':>15}",
#     f"\n{'5. Апельсины:':>15}",
# )
fruts_list = ['Бананы', 'Яблоки', 'Груши', 'Черешня', 'Апельсины']
for i in range(len(fruts_list)):
    print(str(i+1) + '. ' + "{:>10}".format(str(fruts_list[i])))

#Task 2
a = fruts_list
print(a)
vegetable_list = ['Огурцы', 'Помидоры', 'Яблоки', 'Редис']
b = vegetable_list
print(b)
# Или так
# b.index('Яблоки')
# del b[2]
# print(b)
b.remove('Яблоки')
print(b)
# Или так?
# b.index('Яблоки')
# del b[2]
# print(b)

#Task 3
w = [15, 2, 3, 44, 5, 6, 78, 8, 9, 10]
new_w = []
for i in w:
    if i % 2 == 0:
        i /= 4
        new_w.append(i)
    elif i % 2 != 0:
        i *= 2
        new_w.append(i)
print (new_w)