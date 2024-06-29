# Задача №2. Решение в группах

# Пользователь вводит текст(строка). Словом считается последовательность непробельных 
# символов идущих подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.

# Пример 1:

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13

# Пример 2:

# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.

# Output: 19


# Решение 1:

# Для решения этой задачи можно воспользоваться следующими шагами:

# 1. Разбить текст на слова, используя метод .split(), который по умолчанию разделяет 
# строку по пробелам.
# 2. Преобразовать все слова к одному регистру (например, к нижнему), чтобы избежать 
# дублирования слов, которые различаются только регистром.
# 3. Использовать множество (set) для хранения уникальных слов, так как множество 
# автоматически удаляет дублирующиеся элементы.
# 4. Определить количество уникальных слов, используя функцию len() для множества.

def count_unique_words(text):
    # Разбиваем текст на слова, приводим к нижнему регистру и помещаем в множество
    words = set(text.lower().split())
    
    # Возвращаем количество уникальных слов
    return len(words)

# Пример использования
input_text = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""

unique_word_count = count_unique_words(input_text)
print(unique_word_count)

# Этот код выполняет следующие шаги:
# 1. text.lower().split() - разбивает текст на слова и преобразует их к нижнему регистру.
# 2. set() - создаёт множество из слов, автоматически удаляя дублирующиеся.
# 3. len() - вычисляет количество уникальных слов в множестве.


# Решение 2:

def count_unique_words(text):
    # Разбиваем текст на слова, используя split(), и приводим к нижнему регистру
    words = text.lower().split()
    
    # Создаем множество уникальных слов
    unique_words = set(words)
    
    # Возвращаем количество уникальных слов
    return len(unique_words)

# Пример использования
input_text = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""

unique_word_count = count_unique_words(input_text)
print(unique_word_count)

# Этот код выполняет те же шаги, но более явно:
# 1. text.lower().split() - разбивает текст на слова и приводит их к нижнему регистру.
# 2. set(words) - создаёт множество уникальных слов.
# 3. len(unique_words) - вычисляет количество уникальных слов в множестве.