'''''''''словари  (dict)'''''''''''

# изменяемый тип данных не индексируемым 
# упорядеченный итерируемый тип данных 

# {ключ: значение } 
# {} литералы 
# """"""" способы создание словарей""""""""
# # dict_ = {}
# # print (type(dict_))


# dict_ = {'a': 'hello'}
# print (type(dict_))

# dict_1 = dict(a='hello',b=1)
#  print(dict_1)

# ключ должен быть не изменяемым типом данных 
# {[]: 1} - > typeError: unhashable type
 
 # ключи должны быт уникалными 


 # a = {1: 'hello', 1: 'world', 1: 1}
 











# dict_ = dict (['abc', 'cd','ef'])

''''''''''методы словорей'''''''''
# print(dir(dict))
# dict.items()


# for i in dict_:
    # print(i)

# dic.items() возвращает все пары в слоары в виде списка с кортежом 
# print (dict_items()) # dict_etems([()])

# for key, value in dict_.etems(): 
        # print(i)
        # print(key, '--->',value)


# a, b, c  = (1,2,3)
# print(a, '---->',b, '----->', c)




# dict.values() -> для получения всех значений в словаре

# print (dict_.valus())
 # for i in dict_.values(): 
 # print(i)
 # dict.keys() ->  для получение всех ключей словаря 


# print (dict_.key())
# for i in dict_.keys()
# print (i)
#dict.clear() -> очищает  обект словар
#del dict_  удоление обекта


# dict.copy()   возврощает копия словаря

# dict. fromkeys (seq, [default]) > создает словар с ключами из последователности и значением default (none)
# list_ = ['name', 'hello','test']
# dict_ = dict.fromkeys(list_, 1)
# print(dict_)
# dct = dict.fromkeys("as")
# print(dct)
# dict.get(key, [default]) -> взврашает значение по ключу если такого ключа нет не бросает исключение а вызывает ошибку а
# возврашает default .если дефаулт не указан возврашает none


# dict_ = [1: 'one',2: 'two']
# print(dict_.get(1, 'no such key')) # one
# print(dict_.get(3)) # none
# print(dict_[3]) # KeyError
# dict.update(new_dict)  > добовляет толко одну пару

# number = int(input())
# if number < 0:
#     print(False)
# elif number > 0:
#     print(True)
# else:
#     print(True)

# number = int(input())
# if number < 0:
#     print(False)
# elif number > 0:
#     print(True)
# else:
#     print(True)




# string = str(input())
# if len(string) > 5 :
#     print(True)
# else:
#     print(False)
# mark = int(input())
# if mark >= 90:
#     print('Отлично ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, Ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, Ваша оценка 3!0')
# elif mark >= 60:
#     print('Вам стоит подучить материал,')
# else:
#     print('Вы не сдали экзамен.')


# Если число отрицательное вывести строку negative,

# если положительное то positive,

# если number равно 0 то вывести zero.

# Для проверки кода введите значение в поле во вкладке INPUT.

# Например, если в number число:

# number = int(input())
# if number < 0:
#     print('negative')
# elif number > 0:
#     print('positive')
# elif number == 0:
    # print('zero')
#lse: 
    #print('не правилная операция')


# x = 24
# y = 42 
# print(max(x, y))
# x = 22
# def new_func(x):
#     y = 1
#     z = 42
#     if x == y and z == y and x == z:
#         print(3)
#     elif x == y or y == z or z == x:
#         print(2)
#     else: 
#         print(0)

# new_func(x)



# x = int(input('Введите первое число: '))
# y = int(input('Введите второе число: '))
# if x % y == 0:
#     print(x //y)
# else:
#     print(x / y)
#     print(x % y)




year = int(input('ввыедите год: '))
if year % 4 == 0 and year % 100 != 0 or year %  400 == 0:
    print('YES')
else:
    print('No')
    