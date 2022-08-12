a = 0
b = 0
while id(a)  == id(b):
    a -= 1
    b -= 1
print(a, id(a))

a = 5
b = 3+2
print(id(a), id(b))

c = 1232222
d = 1232222


print(c == d)
# True
print(c is d)
# False

L = ['Hello', 'world']
M = L
print(M is L)
M.append('!')
print(L)

M = L.copy()
print(M is L)
# False


#Задание 6.2.8
print('#Задание 6.2.8')
#
#Впишите вместо знаков «?» операцию сравнения идентификаторов списков до и после обновления, чтобы программа распечатала True, если они равны, иначе — False.

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])
print(shopping_center)

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(shopping_center)

print(list_id_after, list_id_before)
print(list_id_after is list_id_before)
print(list_id_after == list_id_before)
print(id(list_id_after), id(list_id_before))
print(id(list_id_after) == id(list_id_before))

print()
print()
#Задание 6.2.9
#Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.
print('#Задание 6.2.9')
s = "aslsadsns"
print(len(set(s)))

text = '''        The Zen of Python
        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!'''
print(len(set(text)))


#Задание 6.2.11
#Найдите ошибку в коде и перепишите строку с ошибкой полностью. Представленная ниже программа должна находить множество символов, которые встречаются в двух строках одновременно.
print('#Задание 6.2.11')

a = 'abcdef'
b = 'ab123'

a_set, b_set = set(a), set(b) # используем множественное присваивание
print(a_set, b_set)

a_and_b = a_set.intersection(b_set)

print(a_and_b)



#Задание 6.2.12
#Напишите программу, которая на вход получает две последовательности целых чисел, а возвращает список элементов, встречающихся
# только в одной из последовательностей. Какую операцию над множествами вы использовали? Введите только название метода без скобок.
print('#Задание 6.2.12')
a_set = {1,2,3,4,5,6,7,8}
b_set = {2,4,6,8,10,12}
print(a_set, b_set)

a_b_diff = a_set.symmetric_difference(b_set)

print(a_b_diff)


a = '' # пустая строка

b = a if a is not None else 1
#the same as:
b = a or 1

print(b)
print( 1 and "hello" and [False])
# [False]
print(42 and 0 and '' and False)
# 0
print([] or 3.14 or False)
# 3.14
print(0 or '' or False)
# False
print()

#Задание 6.3.4
#Что выведет программа?
print('#Задание 6.3.4')
a = "foo"
b = "bar"

print(1 and a or b)

#Задание 6.3.5
#Что выведет программа?
print('#Задание 6.3.5')
a = ""
b = "bar"

print(1 and a or b)

print()
#Задание 6.3.6
#Замените знаки «?» корректным выражением
print('#Задание 6.3.6')

a = ''
b = 1
# пусть a и b - переменные, которые мы хотим проверитьif??? : # проверка истинности обеих переменных
if a and b:
    print("Обе переменные истинные")
    print(a,b)

print()
#Задание 6.3.7
#Замените знаки «?» корректным выражением
print('#Задание 6.3.7')

# пусть a и b - переменные, которые мы хотим проверитьif??? :
a = ''
b = 1
if a and b:
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print( a or b ) # печать значения одной переменной, которая является истинной

print()
#Задание 6.3.8
#Программа должна выводить «Обе переменные ложные», если они являются таковыми. Дополните условный оператор последним блоком.
print('#Задание 6.3.8')
a = ''
b = 0
if a and b:
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print( a or b ) # печать значения одной переменной, которая является истинной
else:
    print("Обе ложные")

print()
#Задание 6.3.9
print('#Задание 6.3.9')
#является ли оно целым, находится ли в определённом промежутке (например, от 100 до 999 включительно),
# да ещё и делится ли на 2 и 3 одновременно. Очень много условий.

a = 204
if 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
        print('Match')

if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")

print()
#Задание 6.3.11
print('#Задание 6.3.11')
#Напишите программу, которая на вход принимает последовательность целых чисел и возвращает True при вводе любых
# чисел и False, если ввести последовательность из нулей.
num = "1 2 3 4 5 6"
num = "0 0 0 0 0"
#num = "1 0 0 0 0"
num_list = list(map(int, str(num).split()))
print(num_list)
print(all(num_list))
print(not any(num_list))



list_tuples = [(i, i**2) for i in range(1,11)]
print(list_tuples)

matrix = [ [i*j for j in range(1,11)] for i in range(1,11)]
#print(matrix)

print()
#Задание 6.3.15
print('#Задание 6.3.15')
#Модифицируйте последний пример таким образом, чтобы в список сохранялось True, если элемент чётный, и False, если элемент нечётный.
#L = [(int(input())%2 == 0 ) for i in range(5)]
list_num = [1,2,3,4,5]
L = [(i % 2 == 0 ) for i in list_num]
print(L)
print(any(L))

print()
#Задание 6.3.16
print('#Задание 6.3.16')
#Подумайте, как нужно записать логическое выражение, используя all([ ]) и any([ ]) над списком чётности, если его
#результат будет истинным тогда и только тогда, когда в списке есть хотя бы один чётный и хотя бы один нечётный элемент.
list_num = [1,3,5,7,8]
L = [(i % 2 == 0 ) for i in list_num]
print(L)
print(any(L))
print(all(L))
print(any(L) and (not all(L)))


print()
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1

print()
#Задание 6.3.17
print('#Задание 6.3.17')
#Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков L и M.
N = [i*j for i,j in zip(L,M)]
print(N)

print()
#Задание 6.3.18
print('#Задание 6.3.18')
#Реализуйте программу, которая сжимает последовательность символов. На вход подаётся последовательность вида
string = 'aaabbccccdaa'
last = text[0] # сохраняем первый символ
count = 0 # заводим счетчик
result = '' # и результирующую строку
si = 1
for i in range(1, len(string)):
    #print(i, string[i])
    if string[i] == string[i-1]:
        si += 1
    else:
        print(string[i-1], si)
        si = 1
print(string[i], si)

print()
text = 'aaabbccccdaaaa'
last = text[0] # сохраняем первый символ
count = 0 # заводим счетчик
result = '' # и результирующую строку
for s in text:
    if last == s:
        count += 1
        last = s
    else:
        result += last + str(count)
        last = s
        count = 1
result += last + str(count)
print(result)


print()
#Задание 6.4.1
print('#Задание 6.4.1')

def linear_solve(a, b):
    if a: # помним, что 0 интерпретируется как False, иначе True
        return b/a
    elif not a and not b:
        return "Бесконечное количество корней"
    else:
        return "Нет корней"
print(linear_solve(2, 9))
print(linear_solve(0,1))

print()
#Задание 6.4.3
#Напишите функцию D(a,b,c), возвращающую дискриминант квадратного уравнения.
print('#Задание 6.4.3')
def D(a, b, c):
    return b**2 - 4*a*c

print()
#Задание 6.4.4
#Реализуйте функцию quadratic_solve(a,b,c), возвращающую «Нет вещественных корней» в случае отрицательного дискриминанта.
#Модифицируйте функцию quadratic_solve(a,b,c), чтобы она возвращала единственный корень при условии нулевого дискриминанта
def quadratic_solve(a,b,c):
    print(a,b,c)
    if D(a, b, c) < 0:
        return "Нет вещественных корней"
    elif D(a, b, c) == 0:
        return -(b/(2*a))
    else:
        return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)

L = [1,0,-1]
print(quadratic_solve(*L))

M = {'a' : 1,
     'b' : 0,
     'c' : -1}

print(quadratic_solve(**M))

print()
#Задание 6.4.9
#Напишите рекурсивную функцию, находящую минимальный элемент списка без использования циклов и встроенной функции min().
print('#Задание 6.4.9')
def min_rec1(l, index=0, min_elm=100):
    print(min_elm, index)
    if index == len(l)-1:
        return min_elm
    if min_elm > l[index]:
        min_elm = l[index]
    min_rec(l, index+1, min_elm)

def min_rec(l):
    print(l)
    if len(l) == 1:
        return l[0]
    #return l[0] if l[0] < min_rec(l[1:]) else min_rec(l[1:])
    if l[0] < min_rec(l[1:]):
        return l[0]
    else:
        return min_rec(l[1:])


L = [10,2,3]
print(min_rec(L))

print()
#Задание 6.4.10
#Напишите рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули.
print('#Задание 6.4.10')
print(12345//10)
print(12345%10)
print(2//10)
print(2%10)

def number_mirror(n, res=0):
    print(n, res)
    if n == 0:
        return res
    else:
        return number_mirror(n // 10, (res*10) + (n % 10))

num = 12345
print(number_mirror(num))


print()
#Задание 6.4.11
#еализовать функцию equal(N, S), проверяющую, совпадает ли сумма цифр числа N с числом S
#При написании программы следует обратить внимание на то, что если S стала отрицательной, то необходимо сразу вернуть False.
print('#Задание 6.4.11')

def equal(N, S):
    print(N,S)
    if S < 0:
        return False
    if N < 10 :
        return N == S
    else:
        return equal(N//10, S - N%10)

num = 432
sum_digits = 2
print(equal(num, sum_digits))



