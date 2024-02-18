# Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає довжину найдовшої 
# пікової підпослідовності. Для формування пікової підпослідовності необхідно мінімум 3 числа. Пікова 
# підпослідовність визначається як послідовність чисел, яка починається з меншого числа, після чого 
# наступне число строго більше попереднього, поки вони не досягнуть вершини (максимального значення у 
# підпослідовності). Всі значення після досягнення вершини мають бути завжди меншими від попередника.
# Наприклад, пікова послідовність може мати вигляд:
# 1 7 2 Де 7 - є вершиною послідовності
# 1 2 3 - не є піковою послідовністю (немає лівої частки) 3 2 1 - також не є піковою полідовністю 
# (немає правої частки) -1 -5 -1 - теж не є піковою послідовністю (необхідно знайти вершину, а не впадину)
# У масиві може бути декілька пікових підпослідовностей, необхідно знайти довжину максимальної
# Приклад Для вхідного масиву: 1, 3, 5, 4, 2, 8, 3, 7, знайдена найдовша пікова 
# підпослідовність має довжину 5 - 1, 3, 5, 4, 2
# Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку 
# unittest та перевірити сценарії коли: всі елементи масиву посортовані за зростанням, 
# посортовані за спаданням, масив з 2х елементів, не містять пікових підпослідовностей, 
# містять 3 пікові послідовності

def peek_sequence(nums):
    k = 1
    cur_peek = 0
    peek_s = []
    cur_seq = []
    while k < len(nums) - 1:
        if nums[k - 1] < nums[k] and nums[k] > nums[k + 1]:
            cur_peek = k
            while cur_peek -1 >= 0 and nums[cur_peek] > nums[cur_peek - 1]:
                cur_seq.insert(0, nums[cur_peek - 1])
                cur_peek -= 1
            cur_peek = k 
            cur_seq.append(nums[cur_peek])
            while cur_peek < len(nums) - 1 and nums[cur_peek] > nums[cur_peek + 1]:
                cur_seq.append(nums[cur_peek + 1])
                cur_peek += 1
            if len(peek_s) < len(cur_seq):
                peek_s = [i for i in cur_seq]
                cur_seq = []
            cur_seq = []
        k += 1
    return peek_s

# print(peek_sequence([1, 3, 5, 4, 2, 8, 3, 7, 6, 5]))
# print(peek_sequence([1, 3, 5, 4, 2, 8, 3, 7, 6, 5, 4, 3, 2, 1]))


################# Variant 1 not completed ################
# def two_dimensional_array_traversal_by_zigzag(m, n):
#     if m == 0 or n == 0:
#         return "Invalid values"
#     if m == 1 and n == 1:
#         return [1]
#     result = []
#     to_top = True
#     i = 1 
        
#     while len(result) < m * n:
#         if len(result) == 0:
#             result.append(i)
#             to_top = False
#         if to_top:
#             result.append(i)
#             while i - (n - 1) >= 0:
#                 i -= n - 1
#                 # print(i)
#                 result.append(i)
#             to_top = False
#         if not to_top:
#             i += 1
#             if i not in result:
#                 result.append(i)
#             while i < m * n:
#                 i += (n - 1)
#                 result.append(i)
#                 if i + n + 1 < m * n:
#                     i += n
#                     break
#             to_top = True
#     return result


# print(two_dimensional_array_traversal_by_zigzag(3, 3))