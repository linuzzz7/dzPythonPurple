user_input = input("Введите сумму: ").split()

if len(user_input) == 4:
    if user_input[0].isdigit() and user_input[2].isdigit():
        rubles = user_input[0]
        kopecks = user_input[2]
        print(f'{rubles}.{kopecks} P')
        exit()

if len(user_input) == 2:
    if user_input[0].isdigit():
        rubles = user_input[0]
        kopecks = "00"
        print(f'{rubles}.{kopecks} P')
        exit()
        
print('Некорректный формат суммы')
