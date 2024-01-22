from itertools import permutations
# Функция для различных комбинаций
def comb(nums: list[int]) -> list[list[int]]:
    return [list(i) for i in set(permutations(nums))] # set для избегания повторов

if __name__ == '__main__':
    nums = []
    N = int(input('Введите количество чисел: '))
    print('Введите числа: ')

    for i in range(N):
        x = int(input())
        nums.append(x)

    print(comb(nums))