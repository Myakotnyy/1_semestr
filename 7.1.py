def spisoksanty(userlist):
    userdict = {}
    for user in userlist:

        # Если количество элементов = 1, то записано только имя
        if len(user) == 1:
            name = user[0]
            index = None
            
        # Присваиваем значения в соответствующем порядке
        else:
            name, index = user
        userdict[name] = index
    return userdict

def main():
    users = [["Rulon Oboev", 777], ["Mars Plutonov"], ["Snikers Zubovich", 767], ["Twiks Karamelevich", 676]]
    result = spisoksanty(users)
    print(result)
if __name__ == "__main__":
    main()