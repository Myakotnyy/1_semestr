# Функция для проверки количества открывающих и закрывающих скобок
def kolvoskob(a: str) -> bool:
    strskob = []

    for i in a:
        strskob.append(i)

    krug = 0
    figur = 0
    kvadrat = 0
    flag = True

    for i in range(len(a)):
        if a[i] == '(':
            krug += 1
        elif a[i] == ')':
            krug -= 1
        elif a[i] == '{':
            figur += 1
        elif a[i] == '}':
            figur -= 1
        elif a[i] == '[':
            kvadrat += 1
        elif a[i] == ']':
            kvadrat -= 1

        if (krug < 0) or (figur < 0) or (kvadrat < 0):
            flag = False
            break

    if (krug != 0) or (figur != 0) or (kvadrat != 0):
        flag = False

    if vnut(a) == False:
        flag = False

    return flag

# Функция для проверки соответствия открывающих и закрывающих скобок
def vnut(a: str) -> bool:
    flag2 = True

    for i in range(len(a) - 1):
        if (a[i] == '{') and ((a[i + 1] == ']') or (a[i + 1] == ')')):
            flag2 = False
        if (a[i] == '[') and ((a[i + 1] == '}') or (a[i + 1] == ')')):
            flag2 = False
        if (a[i] == '(') and ((a[i + 1] == ']') or (a[i + 1] == '}')):
            flag2 = False

    return flag2


def main() -> None:
    a = input()

    if kolvoskob(a):
        return print(True)
    
# Если в заданной строке не  все скобки закрыты или соответствуют, то ищем макисмальную    
    else:
        nowstr = ''
        maxstr = ''
        krug = 0
        figur = 0
        kvadrat = 0

        for n in range(len(a)):
            nowstr = ''

            for i in range(n, len(a)):
                if a[i] == '(':
                    krug += 1
                elif a[i] == ')':
                    krug -= 1
                elif a[i] == '{':
                    figur += 1
                elif a[i] == '}':
                    figur -= 1
                elif a[i] == '[':
                    kvadrat += 1
                elif a[i] == ']':
                    kvadrat -= 1

                nowstr += a[i]

                if kolvoskob(nowstr):
                    if len(nowstr) > len(maxstr): maxstr = nowstr

        if maxstr == '':
            return print(False)
        
        else:
            return print(maxstr)

if __name__ == "__main__":
    main()