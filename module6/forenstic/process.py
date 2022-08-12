import subprocess
import re
import psutil


# пишем функцию, которая возвращает список словарей (from typing import List, если хотите )
def check_active_connections() -> list:
    """ Returns list of all listening connections """

    # import subprocess не забываем, модуль идёт в комплекте, его не надо устанавливать через pip
    # subprocess - это почти что то же самое, что написать какую-либо команду в консоль
    # метод check_output() принимает список, где первый элемент - команда, а все последующие - параметры для команды,
    # в нашем случае  -na
    # мы получаем фактически то же самое, что вывелось бы нам на экран в консоли, и записываем это в переменную output
    output = subprocess.check_output(['netstat', '-na']).decode('cp866')

    # находим все пробелы, чтобы в дальнейшем распарсить нашу строку на словарь
    spaces = re.findall(r'\s+', output)
    strings = output.split('\n')

    # заменяем несколько пробелов в строке на один пробел, чтобы потом понимать, где именно лежит какой параметр
    for space in spaces:
        for i in range(len(strings)):
            strings[i] = strings[i].replace(space, ' ')

    listening = []

    print(len(strings))

    # в каждой строке теперь есть следующая инфа которую удобно распарсить
    # не забываем, что списки начинаются с 0!!!
    for string in strings:
        if string.find('LISTENING') > 0:
            splited = string.split(' ')
            listening.append(
                {
                    'type': splited[1], # элемент 1 - это тип подключения
                    'adress': splited[3], # элемент 3 - адрес, с которого установлено соединение
                    'status': splited[4].strip(), # аргумент 4 - это состояние нашего подключения
                }
            )

    # возвращаем список словарей
    return listening

#for p in check_active_connections():
#    print(p)



def get_running_proccesses() -> list:
    """
    The get_running_proccesses function returns a list of all running processes on the system.

    :return: A list of all the running processes
    :doc-author: Trelent
    """
    processes_iter = psutil.process_iter()

    processes_list = []

    for process in processes_iter:
        processes_list.append(
            {
                'name': process.name(),
                'pid': process.pid,
                'memory used': process.memory_info().vms / 1024 ** 2
            }
        )

    processes_list = sorted(processes_list, key=lambda x: x['memory used'], reverse=True)
    for p in processes_list:
        print(p)


get_running_proccesses()