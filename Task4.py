# Пересечение двух неупорядоченных наборов целых чисел

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
# наборах.

# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки.

# На входе:
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел

# На выходе:
# 3 5

"""
Для решения этой задачи можно использовать множества (set) в Python, поскольку они 
автоматически удаляют дублирующиеся элементы и поддерживают эффективные операции 
пересечения.

Вот как можно реализовать это решение:
1. Сначала считываем входные данные.
2. Преобразуем строки с элементами множеств в списки целых чисел.
3. Используем множества для нахождения пересечения элементов.
4. Сортируем результат и выводим его в виде строки.
"""

def find_common_elements(var1, var2, var3):
    # Разбираем количество элементов
    n, m = map(int, var1.split())
    
    # Преобразуем строки с элементами в списки целых чисел и создаем множества
    set1 = set(map(int, var2.split()))
    set2 = set(map(int, var3.split()))
    
    # Находим пересечение множеств и сортируем результат
    common_elements = sorted(set1 & set2)
    
    # Преобразуем результат в строку и выводим
    return ' '.join(map(str, common_elements))

# Пример использования
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

result = find_common_elements(var1, var2, var3)
print(result)
