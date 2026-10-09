n = int(input("Введите количество чисел (n >= 1): "))

first_num = int(input("Введите число 1: "))
minimum = first_num
maximum = first_num
total_sum = first_num

for i in range(2, n + 1):
    num = int(input(f"Введите число {i}: "))
    total_sum += num
    
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

average = total_sum / n

print(f"Минимум: {minimum}")
print(f"Максимум: {maximum}")
print(f"Сумма: {total_sum}")
print(f"Среднее арифметическое: {average}")
