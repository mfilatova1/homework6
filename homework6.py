my_dict = {'Marina' : 1995, 'Anton' : 2001}
print(my_dict)
print(my_dict['Marina'])
print(my_dict.get('Olga' , 'такого ключа нет'))
my_dict.update({'Oleg' : 1987 , 'Kristina' : 1999})
print(my_dict)
a = my_dict.pop('Marina')
print(a)
print(my_dict)
my_set = {1, 2, 3, 4, 5, 5, False, True, 'summer'}
print(my_set)
my_set.add(6)
my_set.add(7)
my_set.discard(1)
print(my_set)