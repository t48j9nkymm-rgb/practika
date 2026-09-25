n = int(input())

if n < 0 or n > 36:
    print("ошибка ввода")
elif n == 0:
    print("зеленый")
elif 1 <= n <= 10 or 19 <= n <= 28:
    print("красный" if n % 2 == 1 else "черный")
else:
    print("черный" if n % 2 == 1 else "красный")