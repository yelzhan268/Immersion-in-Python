# Задача 2. Модуль для удаления дублирующихся подряд символов
def remove_consecutive_duplicates(s):
    if not s:
        return s
    result = [s[0]]

    for char in s[1:]:
        if char != result[-1]:
            result.append(char)

    return ''.join(result)
