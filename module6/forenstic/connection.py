import socket

def check_is_port_opened(port: int) -> bool:
    '''
    :param port:
    :return:
    '''

    opened = False # переменная открытого порта устанавливается изначально в False
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))

        sock.listen()
        sock.close()
    except socket.error:
        # если возникла ошибка, то не меняем переменную, она остаётся в False
        pass
    else:
        # если код выполнился без ошибки, значит, мы смогли установить прослушку порта, а значит, он был открыт
        opened = True

    # возвращаем логическое значение
    return opened

for i in range(8990, 9010):
    print(f'Port {i} open - {check_is_port_opened(i)}')
