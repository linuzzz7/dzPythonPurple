user_input = input("Введите сумму: ").lower().split()

if len(user_input) == 4:
    if (user_input[0].isdigit() and user_input[1] == "руб"
            and user_input[2].isdigit() and user_input[3] == "коп"):
        rubles = user_input[0]
        if len(user_input[2]) != 2:
            kopecks = "0" + user_input[2]
        else:
            kopecks = user_input[2]
        print(f'{rubles}.{kopecks} {chr(8381)}')
        exit()

if len(user_input) == 2:
    if user_input[0].isdigit() and user_input[1] == "руб":
        rubles = user_input[0]
        kopecks = "00"
        print(f'{rubles}.{kopecks} {chr(8381)}')
        exit()

print('Некорректный формат суммы')
