def pribliz_sum(N: int, nums: list[int], C: int) -> list[str, tuple[list[int], int]]:
    if N <= 4:
        return 'no solution'

    nums.sort()
    bestraznit = float('inf') # Cоздание положительной бесконечности для дальнейшего равнения
    bestlist = None

    for i in range(N - 3): # Задается таким образом, чтобы осталось 3 свободных "слота"
        for j in range(i + 1, N - 2): # Задается так, чтобы была после i и оставалось 2 свободных "слота"
            left = j + 1 # Идет после j
            right = N - 1 # Всегда последнее значение

# Находим лучший вариант суммы и комбинацию чисел
            while left < right:
                nowsum = nums[i] + nums[j] + nums[left] + nums[right]
                nowraznit = abs(C - nowsum)

                if nowraznit < bestraznit:
                    bestraznit = nowraznit
                    bestlist = [nums[i], nums[j], nums[left], nums[right]]

                if nowsum < C:
                    left += 1
                    
                else:
                    right -= 1

    return sum(bestlist), bestlist

if __name__ == '__main__':
    nums = []
    N = int(input('Введите количество чисел: '))
    print('Введите числа: ')
    for i in range(N):
        x = int(input())
        nums.append(x)
    C = int(input('Введите цель: '))

    print(pribliz_sum(N, nums, C))