def f(list1: list[int], list2: list[int]) -> tuple[list[int], list[int], list[int], list[int]]: # ф-ция для сравнения 2-х списков
    nums1 = set(list1)
    nums2 = set(list2)

    double = nums1.intersection(nums2)
    colvo1 = len(double)
    colvo2 = 0
    colvo3 = 0
    colvo4 = 0
    rez1 = list(double)
    rez2 = []
    for i in list1 + list2:
        if i not in double:
            rez2.append(i)
            colvo2+=1
    rez3 = []
    for i in list1:
        if i not in double:
            rez3.append(i)
            colvo3+=1
    rez4 = []
    for i in list2:
        if i not in double:
            rez4.append(i)
            colvo4+=1 

    print('1 ',rez1,colvo1)
    print('2 ',rez2,colvo2)
    print('3 ',rez3,colvo3)
    print('4 ',rez4,colvo4)

if __name__ == '__main__':
    list1 = []
    N = int(input('Введите количество чисел первого списка: '))
    print('Введите числа: ')

    for i in range(N):
        x = int(input())
        list1.append(x)

    list2 = []
    M = int(input('Введите количество чисел второго списка: '))
    print('Введите числа: ')

    for i in range(M):
        y = int(input())
        list2.append(y)
    print(f(list1, list2))