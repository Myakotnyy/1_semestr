def perevod(startnum: str) -> int:
    rimslovar = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    result = 0
    i = 0

    while i < len(startnum):
        # Если рядом стоящие символы образуют пару, то рассматриваем их вместе
        if i < len(startnum) - 1 and startnum[i:i+2] in rimslovar:
            result += rimslovar[startnum[i:i+2]]
            i += 2
            
        # Если символ самостоятельный, то прибавляем значение из словаря
        else:
            result += rimslovar[startnum[i]]
            i += 1
    return result

if __name__ == '__main__':
    startnum = input('Римское число: ')
    print('В арабской системея: ',perevod(startnum))