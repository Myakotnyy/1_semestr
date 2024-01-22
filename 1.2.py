def back(n):
    # Создаем строку для хранения знака числа
    z = ""
    if n < 0:
        z = "-"

    # Преобразование числа в строку, переворот строки 
    n = str(abs(n))[::-1]
    while n[0] == "0":
        n = n[1:]

    # Обратную строку преобразуем в число с учетом знака
    n = int(z + n)
    
    # Проверяем на заданный диапазон [-128, 127]
    if (-2)**7 > n or (2**7 - 1) < n:
        return "no solution"
    else:
        return n

if __name__ == "__main__":
    print(back(int(input())))