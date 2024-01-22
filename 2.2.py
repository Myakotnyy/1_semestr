def coolstr(s):
    # Разделяем строку по пробелам 
    s1 = s.split()

    # Меняем порядок слов, делаем первую букву заглавной, объединениняем слова в одну строку
    s2 = " ".join(reversed(s1)).capitalize()
    
    return s2

if __name__ == "__main__":   
    print(coolstr(input()))