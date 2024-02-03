"""Документация """


def calculate_average(num):
    """ Описание работы функции"""
    total = sum(num)
    count = len(num)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
