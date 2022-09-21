num_list = [4,6,8]
N = 10
print(num_list)
for i in range(len(num_list)):
    print(num_list[i])

for i in range(1,len(num_list)):
    tmp = num_list[i]
    print("i", tmp, i)
    j = 0
    while tmp > num_list[j]:
        print("j", tmp,j)
        j += 1
    print("ij", i, j)
    for k in range(i-1,j-1,-1):
        print("k", tmp, k)
        num_list[k+1] = num_list[k]
        print("k", num_list)
    num_list[j] = tmp
    print("f", num_list)


import requests
import bs4

print("TEST")
print("TEST")

a = 100
b = 50
print(a,b)

a = a + b #150
b = a - b # 100
a = a - b # 50

print(a,b)

a = -13
b = 7
print(a,b)

a = a - b # -20
b = a + b # -13
a = b - a # 7

print(a,b)

#
#q, r определяются из формулы: a = b*q+r.
#r — неотрицательно, т.е. больше нуля или равно ему, но строго меньше числа b.
#Иными словами, если мы делим, скажем, на 4, то остаток может быть равен 0, 1, 2 или 3.

a = 22
b = 8
print("Full:", a//b) #  q = 2
print("Rest:", a%b)
print((a//b)*b+(a%b))

a = -22
b = 8
print("Full:", a//b)# хочется получить 2, как и в прошлый раз, но q = -3,
# максимальное число, которое можно нацело разделить на число при условии,
# что остаток будет положительным — это -24.
print("Rest:", a%b)# а остаток остался r = 2
#-22 = 8 * (-3) + 2
print((a//b)*b+(a%b))

a = 22
b = -8
print("Full:", a//b)
print("Rest:", a%b)
print((a//b)*b+(a%b))

a = -31
b = 2
print("Full:", a//b)
print("Rest:", a%b)
print((a//b)*b+(a%b))

print ((31%2) + (-31 % 2))
print (13%-3*3-3**2)

print(round(11*2.5/3,2))
print(round((3.14159**2)/2))

#3.8.1
print("##Задание 3.8.1")
s  = '1 2 3 4 5 6 7'
print('\n'.join(s.split()))

age = 17
my_age = "I'm %d years old" % (age)
print(my_age)

print("I'm %05d years old" % (age))
print("I'm %o years old" % (age))
print("I'm %x years old" % (age))
print("I'm %10.2f years old" % (age))
print("I'm %c years old" % (age))
print("I'm %s years old" % (age))

age = 17.012345
print("I'm %2e years old" % (age))
print("I'm %e years old" % (age))

pi = 31.4159265
print ("%.4e" % (pi))

#3.9
print("##Задание 3.9")

letters = ['a', 'b', 'c', 'd']
letters.append('e')
print(letters[-1])
print(letters[-4])

#3.9.3
print("##Задание 3.9.3")

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[1:4])
print (L[::3])
print (L[-4::-1])
print (L[-1:-4:-1])

#3.9.4
print("##Задание 3.9.4")
L = ['3.3', '4.4', '5.5', '6.6']

print (list (map (float, L)))

string = '1 1 2 3 5 8 13 21 34 55'
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

#3.9.6
print("##Задание 3.9.6")
string = '1 1 2 3 5 8 13 21 34 55'
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(float, list_of_strings)) # cписок чисел
list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]
print(list_of_numbers)
list_of_numbers.append(sum(list_of_numbers))
print(list_of_numbers)

#3.9.10
print("##Задание 3.9.10")
d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))

#3.9.11
print("##Задание 3.9.11")

book = 'book1'
name = 'name1'
year = '2001'

book_list = {'book_name' : book, 'author_name': name, 'issued':year}
print(book_list)

abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}

abit_list = [abit1, abit2, abit3]
print(abit_list)

text = "25 Bloomburg St"
print(text.find('St') )