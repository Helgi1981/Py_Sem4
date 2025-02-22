# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, 
# и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, 
# которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность
# (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система 
# состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий 
# модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль 
# находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое 
# может собрать один собирающий модуль за один заход, находясь перед некоторым кустом 
# грядки.

# Входные данные:
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность 
# i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:
# Программа должна вывести одно целое число - максимальное количество ягод, которое 
# может собрать собирающий модуль, находясь перед некоторым кустом грядки.

# Пример использования 
# На входе:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]

# На выходе:
# 19

"""
Для решения этой задачи нужно учесть, что черничные кусты растут по кругу, поэтому 
необходимо рассмотреть ситуацию, когда собирающий модуль находится перед первым кустом, 
и собирать ягоды с последнего куста как соседа.

Алгоритм решения:
1. Инициализируем переменную для хранения максимального числа ягод.
2. Проходим по каждому кусту и вычисляем сумму ягод для текущего куста и двух его соседей 
(слева и справа). Для этого используем индексные операции, учитывающие циклическую 
природу списка.
3. Обновляем максимальную сумму, если текущая сумма больше.
4. Выводим максимальную сумму ягод, которую может собрать модуль.
"""

def max_berries(arr):
    n = len(arr)
    max_sum = 0

    for i in range(n):
        # Суммируем текущий куст и два соседних (учитываем циклическую природу списка)
        curr_sum = arr[i] + arr[(i - 1) % n] + arr[(i + 1) % n]
        # Обновляем максимальную сумму
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Пример использования
arr = [5, 8, 6, 4, 9, 2, 7, 3]
print(max_berries(arr))  # Output: 19