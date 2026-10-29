operations = []

while True:
    print("===== PERSONAL FINANCE MANAGER =====")
    print()
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. История операций")
    print("4. Показать баланс")
    print("5. Статистика по категориям")
    print("6. Поиск операций")
    print("0. Выход")
    print()
    a = input('Выберете действие: ')

    if a == '1':

        amount = input('Введите значение операции: ')

        if str(amount).isdigit() and int(amount) > 0:
            category = input('Укажите категорию: ')
            amount = int(amount)
            new_operation = {
                "type": "income",
                "amount": amount,
                "category": category
            }
            operations.append(new_operation)
            print('Доход успешно добавлен!')
        else:
            print('Неправильный ввод дохода')



    elif a == '2':


        amount = input('Введите значение операции: ')

        if str(amount).isdigit() and int(amount) > 0:
            category = input('Укажите категорию: ')
            amount = int(amount)
            expense = {
                "type": "lose",
                "amount": amount,
                "category": category
            }
            operations.append(expense)
            print('Расход успешно добавлен!')
        else:
            print('Неправльный ввод расхода')



    elif a == '3':
        print("===== ИСТОРИЯ ОПЕРАЦИЙ =====")
        print()
        if len(operations) < 1:
            print('Введите операции')
        else:
            for using in operations:
                print(f"Тип операции: {using["type"]}")
                print(f"Количество средств: {using["amount"]}")
                print(f"Категория: {using["category"]}")

                print("------------------------")




    elif a == '4':
        balance = 0      # каждый раз вычисляется заново
        print("===== БЮДЖЕТ =====")
        print()
        for operation in operations:
            if operation["type"] == 'income':
                balance = balance + operation["amount"]
            else:
                balance = balance - operation["amount"]
        print(f"Ваш баланс составляет: {balance}")


    elif a == '5':
        print("===== Статистика по категориям =====")
        print()
        statistics = {

        }
        for operation_category in operations:
            if operation_category["type"] == 'lose':

                category = operation_category["category"]
                amount = operation_category["amount"]

                if category not in statistics:
                    statistics[category] = amount
                else:
                    statistics[category] += amount
        
        for category, value in statistics.items():
            print(f"{category} | {value} ₽")


    elif a == '6':
        print('===== Найденные операции =====')
        flag = False
        cat = input('Введите интересующую операцию: ')
        if cat.isalpha():

            for using in operations:
                if using["category"] == cat:
                    flag = True
                    for key, value in using.items():
                        print(f"{key} | {value}")

                    print("------------------------")
            if flag == False:
                print('Категоррия не найдена')
        else:
            print('Неправильный ввод категории')
                

    elif a == '0':
        print('До свидания! Программа завершена')
        break
    else:
        print("Неверная команда")







