x = 1
y = -1
if 0 <= x and 0 <= y:
    pass
if 0 > x and 0 <= y:
    pass
if 0 <= x and 0 > y:
    pass
if 0 > x and 0 > y:
    pass

login_list = [
    'root',
    'username1'
]

password_list = {
    'root': '1q2w3e4r',
    'username1': 'qwerty123'
}

username = 'root'

if username in login_list:
    #password = input('Введите password:\n')
    password = 'ddd'
    if password == password_list[username]:
        print('OK')
    else:
        print('deny')
else:
    print('no such user')

a = 42
b = 41
result = a if a > b else b
print(result)

a = 100
if not (-10 <= a <= -1 and 2 <= a <= 15):
    print('outside')
else:
    print('inside')

a = 46
r = a % 10
p = a // 10
if r == 5 or p == 5:
    print('5 inside')
print((r == 5 or p == 5))

list2 = [0, 1, 2, 3, 4,4 ,3 ,2, 1, 0]
list1 = list(range(5))
print(list1)
if len(list2) == len(set(list2)):
    print('all unique')
else:
    print('not unique')

n = 123443211
str = str(n)
if str == str[::-1]:
    print('polyndrom')
else:
    print('not polindrom')

print((list(range(20,15,-1))))
print((list(range(20,14,-2))))

n = 6
for i in range(1,n+1):
        print('*' * i)


n = 1
while n**2 < 1000:
    res = n ** 2
    n += 1
print(res, n-1)

n = 1
while True:
    if n ** 2 > 1000:
        print('last number', n-1)
        break
    n += 1
print(n)


list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, v in enumerate(list_):
    if list_[i] < 0:
        print("Отрицательное число: ", list_[i])
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", list_[i])
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)


x = 3

def func():
    print(x)
#    x = 5
#    x += 5
    return x
print(func())


def get_mul_finc(m):
    nonlocal_m = m
    def local_mul(n):
        return n * nonlocal_m
    return local_mul

two_mul = get_mul_finc(2)
print(two_mul(5))

print()
print()

def my_func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

my_func()

def adder(*num):
    sum_ = 0
    for n in num:
        sum_ += n
    return sum_
print(adder(1,2,3))

def factor(*num):
    mul_ = 1
    for n in num:
        mul_ *= n
    return mul_
print(factor(1,2,3,7))


def incorrect_func(name_arg=[]):
    # name_arg является локальной переменной
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)

incorrect_func()
print('-----')
incorrect_func()
print('-----')
print('-----')

def correct_func(name_arg=None):
    print("Аргумент до изменения", name_arg)
    if name_arg is None:
        name_arg = []
    else:
        name_arg.append(1)
    print("Аргумент после изменения", name_arg)

correct_func()
print('-----')
correct_func([1,2,3])

def factorial(n):
    if n == 1:
        return n

    return n * factorial(n-1)

print(factorial(5))


def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    return fibonachi(n-1) + fibonachi(n - 2)

print(fibonachi(10))
print(6//10)

print('------')
def sum_num(n):
    if n == 1:
        return 1
    return sum_num(n-1) + n
print(sum_num(4))

print('------')
s = '1234'
print(s[:-1], s[-1])
print('------')
def reverse_str(s):
    print(s)
    if not s:
        return ''
    return s[-1] + reverse_str(s[:-1])
print(reverse_str('1234'))


print('------')
def sum_digits(n):
    print(n)
    if n < 10:
        return n
    return sum_digits(n//10) + n%10
print(sum_digits(1234))


print('----')
def reverse_number(n, res=0):
    print(n, res)
    if n == 0 :
        return res
    return reverse_number(n // 10, res*10+n%10)

print(4//10, 4%10)
print('####')
print(reverse_number(45678))


print('---------')
def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

num = fib()
for i in range(6):
    f = next(num)
    print(f)



print('---------')
def int_num(start=0, step=1):
    a = start
    while True:
        yield a
        a += step


num = int_num(1)
for i in range(4):
    f = next(num)
print(f)

print('---------')
def loop_gen1(arr):
    count = 0
    #yield a
    while True:
        yield arr[count]
        count = count+1 if count+1 < len(arr) else 0

def loop_gen(arr):
    arr_copy = arr.copy()
    while True:
        value = arr_copy.pop(0)
        yield value
        arr_copy.append(value)

num = loop_gen([1,2,3])
for i in range(7):
    f = next(num)
    print(f)


print('---------')
str_ = "my_tst"
str_iter = iter(str_)
print(str_)
print(str_iter)
print(next(str_iter))
print('--')
for s in str_iter:
    print(s)

print('-----')
def adder(x):
    print('external', x)
    def int_func(n):
        print('internal', n)
        return x + n
    return int_func
add_5 = adder(5)
print((add_5(16)))


print('-------')
def my_decor(a_func_to_decorate):
    def wrapper():
        print('before call the function', a_func_to_decorate)
        result = a_func_to_decorate()
        print('after call the function', a_func_to_decorate)
        return result
    return wrapper

def my_function():
    print("Я - оборачиваемая функция!")
    return 0

print(my_function())

print('----')
decorated = my_decor(my_function)
print(decorated())

print('-----')
import time

def decor_time(fn):
    def wrapper():
        time0 = time.time()
        result = fn()
        dt = time.time() - time0
        #print('time to run {:.10f}'.format(dt) )
        return result
    return wrapper


def pow_2():
    return 1000000 ** 2

def in_build_pow():
    return pow(1000000, 2)

pow2 = decor_time(pow_2)
in_build_pow = decor_time(in_build_pow)

print(pow2())
print(in_build_pow())

N = 100
mean_pow_2 = 0
meam_in_build = 0

for _ in range(100):
    mean_pow_2 += pow2()
    meam_in_build += in_build_pow()

print('mean time to run pow2 {:.10f}, total {}'.format(mean_pow_2/N, mean_pow_2))

print('--------------')
def mean_time(n_times):
    def decor_time(fn):
        def wrapper(*arg, **kwargs):
            time0 = time.time()
            for _ in range(n):
                result = fn(*arg, **kwargs)
            dt = time.time() - time0
            print('mean time to run {:.10f} times {}'.format(dt/n_times, n_times) )
            return result
        return wrapper
    return decor_time

mean_100 = mean_time(100)
pow2 = mean_100(pow_2)
in_build_pow = mean_100(in_build_pow)

print(pow2())
print(in_build_pow())


print('-----')
print('###5.5.2')
def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    calls_n = 0
    def wrapper(*args, **kwargs):
        nonlocal calls_n
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        calls_n += 1
        print('Этот код будет выполняться после каждого вызова функции')
        print("number of calls", calls_n)
        return result
    return wrapper

@my_decorator
def my_function():
    return 0

print(my_function())
print(my_function())


print('-----')
print('###5.5.3')

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    dict_results = {}
    def wrapper(*args, **kwargs):
        nonlocal dict_results
        if args[0] not in  dict_results:
            print('Этот код будет выполняться если агрумент НЕ в базе')
            result = fn(*args, **kwargs)
            dict_results[args[0]] = result
        else:
            print('Этот код будет выполняться если агрумент В базе')
            result = dict_results[args[0]]
        return result
    return wrapper


@my_decorator
def f(n):
    return n * 123456789

print(f(11))
print(f(10))
print(f(11))


list_dir = ['melb_data.csv', 'melb_data_fe.zip','citibike-tripdata.csv', 'dates.csv', 'melb_data_fe_module12.csv', 'melb_data_ps.csv', 'melb_data_ps.zip', 'movies.csv', 'movies_data.zip', 'ratings1.csv', 'ratings2.csv', 'ufo.csv']
list_dir.sort()
print(list_dir)