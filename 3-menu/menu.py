food = input('Выберите категорию блюд:\n - напиток - суп - десерт: ')
# food choise
match food:
    case 'напиток':
        drink = input('Выберите напиток: чай, кофе, сок: ')
        match drink:
            case 'чай':
                print('Цена:', 10)
            case 'кофе':
                print('Цена:', 20)
            case 'сок':
                print('Цена:', 15)
    case 'суп':
        soup = input('Выберите суп: борщ, щи, суп-пюре: ')
        match soup:
            case 'борщ':
                print('Цена:', 25)
            case 'щи':
                print('Цена:', 20)
            case 'суп-пюре':
                print('Цена:', 30)
    case 'десерт':
        desert = input('Выберите десерт: торт, мороженное, фрукты: ')
        match desert:
            case 'торт':
                print('Цена:', 25)
            case 'мороженное':
                print('Цена:', 20)
            case 'фрукты':
                print('Цена:', 30)
