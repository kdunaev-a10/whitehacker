import numpy as np

"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""


def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count


def half_predict(number: int=50) -> int:
    """Guess using half/divide

    Args:
        number (int, optional): Number to guess. Defaults to 50.

    Returns:
        int: number of repeats
    """
    range_random = 100
    count = 0
    predict_number = int(range_random / 2)  # предполагаемое число
    min_last = 1
    max_last = range_random
    while True:
        count += 1
        if number > predict_number:
            min_last = predict_number
            predict_number = int((min_last + max_last)/2)

        elif number < predict_number:
            max_last = predict_number
            predict_number = int((min_last + max_last)/2)

        if number == predict_number:
            break  # выход из цикла, если угадали
    return count


def recursive_predict(number, left, right):
    """Guess using half/divide by recursive

    Args:
        left (_type_): the left limit of the range
        right (_type_): the left limit of the range
        number (int, optional): number ot guess

    Returns:
        int: number of repeats
    """
    global count
    predict_number = int((left + right)/2)  # предполагаемое число
    if number > predict_number:
        count += 1
        recursive_predict(number, predict_number, right)

    elif number < predict_number:
        count += 1
        recursive_predict(number, left, predict_number)

    if number == predict_number:
        #  выход из цикла, если угадали
        return


def score_game(func_predict) -> int:
    """
    The score_game function will take a function that randomly guesses a number between 1 and 99
    (inclusive) and returns how many guesses it took to get the right answer.
    The function will also take an integer parameter determining how many times the game is played.
    The score_game function will return the average number of guesses it took to win each game.


    Args:
        func_predict: Pass the function that will be used to predict the number

    Returns:
        int: average of repeats
    """
    range_random = 100
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, range_random, size=1000)
    for number in random_array:
        count_ls.append(func_predict(number))
    score = int(np.mean(count_ls))

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


def score_game_recursive(func_predict) -> int:
    """
    The score_game function will take a function that randomly guesses a number between 1 and 99
    (inclusive) and returns how many guesses it took to get the right answer.
    The function will also take an integer parameter determining how many times the game is played.
    The score_game function will return the average number of guesses it took to win each game.


    Args:
        func_predict: Pass the function that will be used to predict the number

    Returns:
        int: average of repeats
    """
    range_random = 100
    global count
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, range_random, size=1000)
    for number in random_array:
        count = 0
        func_predict(number, 1, range_random)
        count_ls.append(count)
    score = int(np.mean(count_ls))

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


if __name__ == '__main__':
    #    print("Random prediction: ")
    #    score_game(random_predict)
    print("Half-divide prediction: ")
    score_game(half_predict)
    print("Half-divide using recursive prediction: ")
    score_game_recursive(recursive_predict)
