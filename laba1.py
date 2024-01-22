# Создаем функцию расстановки знаков через рекурсию
def reccomb(indeks,sum,znaksum):
    global rez
    global kucha
    if rez != '':
        return 0
    if indeks == len(kucha):
        if sum == S:
            rez = znaksum
        return 0
    reccomb(indeks + 1, sum + int(kucha[indeks]), znaksum+'+'+str(kucha[indeks]))
    reccomb(indeks + 1, sum - int(kucha[indeks]), znaksum+'-'+str(kucha[indeks]))

# Считываем файл и записываем значения в переменные
with open('laba1.txt', "r") as file:
    labstr = file.readline().strip().split()
    N = int(labstr[0])
    S = int(labstr[-1])
# Делаем срез, чтобы отделить первое и последнее значение от основной массы чисел
    kucha = labstr[1:-1]
    rez = ''

# Проверяем на заданный условием диапазон
if N >= 2 and N <=30 and S >= -10**9 and S <= 10**9:
    reccomb(1,int(kucha[0]),str(kucha[0]))
    if rez == '':
        result = 'No solution'
    else:
        result = rez + '=' + str(S)
else:
    result = 'No solution'

def main():
    with open("laba1.txt", "w") as file:
        file.write(result)

if __name__ == "__main__":
    main()