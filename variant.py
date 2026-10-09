import sys

try:
    n = int(input("Введите количество чисел (n >= 0): "))
except ValueError:
    print("Ошибка: введено не целое число.")
    sys.exit()

if n < 0:
    print("Ошибка: n должно быть >= 0")
    sys.exit()

count_positive = 0
sum_positive = 0

print(f"Введите {n} целых чисел (каждое с новой строки):")

for i in range(n):
    try:
        num = int(input())
    except ValueError:
        print("Ошибка ввода. Это значение пропущено.")
        continue
    
    if num > 0:
        count_positive += 1
        sum_positive += num

if count_positive == 0:
    result_1 = 0
    result_2 = 0
else:
    result_1 = count_positive
    result_2 = sum_positive

print("\n--- Результаты ---")
print(f"Результат 1 (Количество): {result_1}")
print(f"Результат 2 (Сумма): {result_2}")
