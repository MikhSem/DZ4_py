# Задача 22:

import random

# Считываем значения n и m от пользователя
n = int(input("Введите количество элементов в первом списке: "))
m = int(input("Введите количество элементов во втором списке: "))

# Создаем и выводим два списка с рандомными числами от 1 до 10 
list1 = [random.randint(1, 10) for _ in range(n)]
list2 = [random.randint(1, 10) for _ in range(m)]
print(f"Первый список: {list1}\nВторой список: {list2}")

# Находим пересечение, сортируем его и выводим результат
print(f"Числа, которые встречаются в обоих списках: {sorted(list(set(list1) & set(list2)))}")


# Задача 24
n = int(input("Введите количество кустов: "))
arr = [random.randint(1, 15) for _ in range(n)]
print("Количество ягод на кустах:", arr)

if n <= 2:
    max_value = sum(arr)
    print("Максимальное количество ягод:", max_value)
else:
    arr_counter = list()
    for i in range(len(arr) - 1):
        arr_counter.append(arr[i - 1] + arr[i] + arr[i + 1])
    arr_counter.append(arr[-2] + arr[-1] + arr[0])

    max_value = max(arr_counter)
    print("Максимальное количество ягод:", max_value)
