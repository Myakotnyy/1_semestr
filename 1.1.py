def palindrome():
    firstnum = int(input())
    # Сохраняем начальное число
    safenum = firstnum
    # Создаем переменную для обратного числа
    secondnum = 0

    if firstnum < 0:
        return False
    
    # Создаем обратное число
    while firstnum > 0:
        secondnum = secondnum * 10 + firstnum % 10
        firstnum = firstnum // 10

    if safenum == secondnum:
        print("Число подходит", safenum , secondnum)
        
    else:
        print("Число не подходит", safenum , secondnum)

if __name__ == "__main__":
    palindrome()