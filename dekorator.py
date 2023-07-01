'''декораторы'''


# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
# inner_func = outer(9)

# print(inner_func(9))


'''
функция высшего порядка - это функция которая может принимат в качестве оргумента другую функцию
или возвращат функцию как резултать 
'''
# def test_func(func):
#     def inner_test_func():
#         # <тело>
#         func()
#     return inner_test_func
# def hello(func):
#     pass

'''декароторы функция высшего порядка 
качествве аргумента принимает функцию и 
возврашает функцию которая оборачивает другую функцию для расширении
ее функционала при этом не изменяя ее код
'''
# def test(func): 
#     print('makers') 
#     func()
#     print('hello')
# def a():
#     print('привет')
# test(a)

# def benchmark(func):
#     # def wrapper():
        
#     import time
#     start = time.time()
#     func()
#     end = time.time()
#     print(f'время работы функции{func.__name__}, заняло {end - start}')
# def loop():
#         i = 0 
#         while i < 100000:
#             print(i)
#             i += 1
# benchmark(loop)


# def decarator(func):
#     def wrapper():
#         print('функция обертки')
#         print('оборачиваем функцию {func.__name__}')
#         func()
#         print('выходим из обертки')
#     return wrapper
# @decarator
# def say_hi():
#     print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
# # say_hi()
# say_hi = decarator(say_hi)
# say_hi()

'''-> синтаксический сахар позволяет нам явно укозать какой декоратор применяется для функции

под капотом вызывает функцию decarator и резултат
выполнении этой функции сохранили в пременной с точно таким 
же название как и обернутая функция 
say_hi = decorator(say_hi)
say_hi()
 '''
# def uppercase_decorator(func):
#     def wrapper():
#         func = func()
#         upper_str = func.upper()
#         return upper_str
#     return wrapper


# @uppercase_decorator

# def inp_str():
#     str_ = input(' ')
#     return str_

# print(inp_str())

