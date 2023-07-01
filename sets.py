''' множество -> set'''
 # измененяемый неупорядоченный
 # не индексируемый итерируемый тип данных который хранит в себе толко уникалные значение 
 # литералы {}
'''создание пустого множество '''
# set_a = set()
# print(type(set_a))
# set_b = {1,2,3}
# print(set_b)

'''элементами множество могут быт толко неизменяемые типы'''


# set_ = set({1: 'a' 2: 'b' 3: 'c'})



#'''методы множества'''

#print (dir(set))
# set.abb(element) -> добовляет element во множество
'''если добавит тюпл то все его элементы должны быт не изменяемыми'''

# set_a = {1,2,3, (1,3, 'hello')}
# set_a.add('a')
# a = 4 
# set_a.add(a) 
# print(set_a)

# for 


# set. update(iterable) - > ддобовляет элемент из последователности во множество

# set_a = {1,2,3,4,5,6, 'hello', 'test', 'world'} 
#set_aupdaet 


# set_a.clear() очищает множество 
# print(set_a)



# set.pop() удоляет рандомно из множество 
# первый в текущем порядке
# set_a = {'world', 1,2,3,4, 'hello'}

#print(set_a)
#print (set_a)
#print(set_a.pop())
#print(set_a)
#print(set_a.pop())
#print(set_a)
#print(set_a.pop())
#print(set_a)


# set.difference(set_b) >  возврощат  элементы которые ест в сет_а но нет в сет_б
# set_a = {1,2,3,4,5}
#set_b{4,5,6,7,8,}
#print(set_a.difference(set_b))
#print(set_b.difference(set_a))


#set_a.symmetric_difference(set_b ) возврощает уникалные элементы сет_ф и для сет_б
# уникалные для обоих множеств

# set_a = {1,2,3,4,5,'hello'}
# set_b = {4,5,6,7,8, 'test'}
# print(set_a.symmetric_dofference(set_b))



#set_a.intersection(set_b) возвращает схожие элементы в обоих множествах

#set_a = {1,2,3,4,5, 'hello', 'test'}
#set_b = {4,5,6,7,8, 'test'}





# set_a.union(set_b) >соидиненяет два множество
#set_a = {1,2,3,4,5, 'hello', 'test'}
#set_b = {4,5,6,7,8, 'test'}
#print(set_a.union(set_b))
#print(set_a | set_b)





