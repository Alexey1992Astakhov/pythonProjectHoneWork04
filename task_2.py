#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def func_mn(num):
    result = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            result.append(i)
    return result


num = int(input(("Введите натуральное число N: ")))

print(f"Результат деления: {func_mn(num)}")