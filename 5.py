def banki() -> list[list[list[int, list[list[str, int]]]], None]:
    kolvo = int(input('Введите кол-во банков: '))
    banks = []
    for _ in range(kolvo):
        name = input("Введите название банка: ")
        moneys = int(input("Введите деньги банка: "))
        banks.append(tuple([name,moneys]))

    money = []
    visited_index = []
    
    if kolvo <= 2:
        # Если банк один, то берем его сумму и индекс
        if kolvo == 1:
            money.append(banks[0][1])
            visited_index.append(0)
        # Если банков два, то берем сумму и индекс банка с максимальным количеством денег
        if kolvo == 2:
            money.append(max(banks[1][1], banks[0][1]))
            if banks[1][1] < banks[0][1]:
                visited_index.append(0)
            else:
                visited_index.append(1)

    else:

        money.extend([banks[0][1], max(banks[1][1], banks[0][1])])

        if banks[1][1] < banks[0][1]:
            visited_index.append(0)
        else:
            visited_index.append(1)


        for i in range(kolvo - 2):
            # Если сумма с банком больше, чем сумма до этого банка, то он добавляется
            if money[i] + banks[i+2][1] > money[i+1]:
                money.append(money[i] + banks[i+2][1])
                visited_index.append(i+2)
                # Убираем лишние индексы неподошедших банков, записываем нужные
                if i+1 in visited_index:
                    visited_index.remove(i+1)
                if i > 0:
                    if i not in visited_index and i - 1 not in visited_index:
                        visited_index.append(i)

            else:
                money.append(money[i+1])
                if i in visited_index:
                    visited_index.remove(i)

    # Создаем список с мксимальной суммой денег
    itog = [money[-1]]
    
    # Добавляем выбранные банки и их индексы в список
    for i in visited_index:
        itog.append((banks[i][0], i+1))


    return itog


if __name__ == "__main__":
    print(banki())