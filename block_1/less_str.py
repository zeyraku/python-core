# word = input()
# flag = True

# for i in range(len(word)//2):
#     if word[i] != word[len(word)-1-i]:
#         flag = False
#         break
# if flag == True:
#     print('Палиндром')
# else:
#     print('Не палиндром')


# stri = input()
# stri = stri.lower().strip()
# if stri == 'python':
#     print(f'Вы ботаете {stri}')
# else:
#     print('Вы ботаете другое')



# tickets = input('Введите названия через запятую: ').split(',') # создается список, где через запятую элементы - строки

# result = []
# for tick in tickets:
#     tick = tick.strip().upper()
#     result.append(tick)

# print(" | ".join(result))





# tickets = input('Введите тикеты через запятую: ').split(',')
# result = []

# for el in tickets:
#     el = el.upper().strip()

#     if (len(el) >= 2 and len(el) <= 5) and (el.isalpha()):
#         result.append(el)
#     else:
#         continue

# print(' | '.join(result))
# print(len(result))


# text = input('Введите команды через ; : ').split(';')
# result = []

# for soo in text:
#     soo = soo.strip()

#     if 'error' in soo.lower():
#         result.append(soo)

# for i in result:
#     print(i)
# print()
# print(f'Количество ошибок: {len(result)}')






# text = input('Введите название и операцию через ;: ').split(';')
# col_buy = 0
# col_count = 0
# array = []

# for i in text:
#     parts = i.strip().split(':')

#     ticker = parts[0].strip()
#     action = parts[1].strip()
#     if action.upper() == 'BUY':
#         col_buy += 1
#         array.append(ticker.upper())
#     elif action.upper() == 'SELL':
#         col_count += 1
    
# print(f'Купленные: {col_buy}')
# print(f'Проданные: {col_count}')
# print()
# print('Тикеры с сигналом BUY:')
# print()
# for i in array:
#     print(i)
# print()
# print(f'Всего корректных сигналов: {col_count + col_buy}')


# btc = 67432.9876
# eth = 3521.4567
# sol = 184.9
# print(f'{'Тикер':<10}{'Цена USDT':>12}')
# print('-' * 23)


# print(f'{"BTC":<10} {btc:>12.2f}')
# print(f'{"ETH":<10} {eth:>12.2f}')
# print(f'{"SOL":<10} {sol:>12.2f}')












