# Напишіть функцію для пошуку k-того найбільшого елемента в заданому масиві цілих чисел. 
# Параметр k задається на вхід функції і визначає порядковий номер найбільшого елемента, 
# який потрібно знайти. Наприклад, якщо k = 1, програма повинна знайти найбільший елемент в масиві. 
# Якщо k = 2, програма повинна знайти другий за величиною елемент, і так далі.
# Умови задачі:
# Масив цілих чисел передається у вашу функцію.
# Розмір масиву повинен бути не менше k.
# Програма повинна вивести k-тий найбільший елемент і його позицію (індекс) в масиві.
# Приклад введення та виведення результату:
# Вхідний масив: [15, 7, 22, 9, 36, 2, 42, 18] Задане k: 3 Знайдений 3-й найбільший елемент: 
# 22 Позиція 3-го найбільшого елемента в масиві: 2
# Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest .

def find_biggsest_el(nums, k):
    not_sorted_list = [i for i in nums]
    if len(nums) < k:
        return f"The list is to small to find the {k} biggest element"
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                is_sorted = False
    
    return nums[-k],  not_sorted_list.index(nums[-k])

print(find_biggsest_el([15, 7, 22, 9, 36, 2, 42, 18], 3))


########### Variant 1 ###########
# def amount_of_seeds_per_field(m, n):
#     robot_road = []
#     i = 0
#     while len(robot_road) <= m*n:
#         if i == m * n:
#             break
#         if i % n == 0 and i > 0:
#             for j in range(i+n, i, -1):
#                 robot_road.append(j)
#                 i += 1 
#             continue
#         for k in range(i+1, i+n+1):
#             robot_road.append(k)
#             i += 1
#     return robot_road

# print(amount_of_seeds_per_field(5, 5))
# print(amount_of_seeds_per_field(3, 4))
