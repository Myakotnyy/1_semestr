def maxcombo(a):
    # Создаем переменные для текущей строки и максимальной строки
    a1 = ""
    max = ""
    
    # Получаем все значения строки кроме последнего
    for i in range(len(a) - 1):
        a1 = a[i]
        
        for j in range(i + 1, len(a)):
            # Проверяем, что следующий символ не повторяется с уже записанными
            if a[j] not in a1:
                a1 = a1 + a[j]
                
                # Перезаписываем максимальную строку
                if len(max) < len(a1):
                    max = a1
            else:
                # Если символ повторяется, обновляем максимальную строку
                if len(max) < len(a1):
                    max = a1
                a1 = ""
                break
    
    return max

if __name__ == "__main__":   
    print(maxcombo(input()))