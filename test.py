a = 'stroka'
print (a)
print (a [0])
print (a [5])
a *=3
a +='abc'
print (a)
lengh = len(a)
print (len(a))
new_a = a[6:19]
print(new_a)
new_a = a [0:20:2]
print(new_a)
a = 'stroka'
a = a[::-1]
print (a)
b = '''a
b
c'''
print (b)
a = 'one two three'
print (a.title())
print (a.capitalize())
print (a.upper())
b = 'ONE TWO THREE'
print (b.lower())
c = 'One Two Three'
print (c.swapcase())
d = 'Hello, {}. your age is {}'. format ('Al', 36, 40, 'Gik')
print (d)
a = 'print hello world and have fun and go home'
print(len(a))
a = a.replace('and', 'or')
b = a.split('.')
a = ['a', 'b', 'c', 5, 'hello']
a[0] = 6
print (a)
my_list = ['a','b']
my_list += [1,2,3]
print (my_list)
model = ['Mod S', 'Mod 3', 'Mod X', 'Mod Y']
my_model = 'amg'
print(my_model in model)
for Tmodel in range(0, len(model)):
    print (model [Tmodel]in model)
my_list = ['one','two']
other_list = ['one', my_list, 'two']
second_list =  ['one',['one','two'],'two']
my_list.append ('three')
print (my_list)
my_list = [1, 2, 3, 4]
my_element = my_list.pop (1)
print (my_list)
my_element = my_list.remove (1)
my_list.insert(3, 'hello')
print (my_list)
my_list = [5,3,4,2,1]
my_list.reverse=True
my_list.clear
my_tuple = (1, 2 , 3, 4, 5)
print (my_tuple)
