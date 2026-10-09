rejected_count = 0

while True:
    number = int(input("Введите положительное число: "))
    if number > 0:
        break
    rejected_count += 1

square = number ** 2

print(f"Квадрат числа: {square}")
print(f"Количество отклонённых попыток: {rejected_count}")
