# Дано відсортований масив цілих чисел nums за зростанням (від менших до більших значень). 
# Напишіть функцію, яка повертає новий масив, в якому кожен елемент є квадратом відповідного 
# елемента з масиву nums. Отриманий масив також повинен бути відсортованим за зростанням.
# Поверніть новий масив відповідно до вхідних даних.
# Вхідні дані: nums = [-4,-2,0,1,3] Результат: [0,1,4,9,16]
# Вхідні дані: nums = [1,2,3,4,5] Результат: [1,4,9,16,25]
# Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку 
# unittest та перевірити роботу вашої функції на прикладах, наведених вище

def square_sorted_list(nums):
    result = [i ** 2 for i in nums]
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(result)):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                is_sorted = False
    return result


print(square_sorted_list([-4, -2, 0, 1, 3]))

# ######### Variant 1 ##########
# def is_subarray(nums1, nums2):
#     count = 0 
#     for num in nums1:
#         if num in nums2:
#             count +=1
#             continue
#     if len(nums1) == count:
#         return True
#     return False
# print(is_subarray([1, 2, 3], [1, 2, 3, 4]))
