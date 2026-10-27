# tickers = ['BTC', 'ETH', 'SOL', 'XRP', 'ADA', 'BNB']
# tickers.remove('SOL')
# time_tik = tickers.pop(-3)
# del tickers[-1]
# print(tickers)


# prices = [67000, 3500, 185, 0.52, 240, 95, 12]
# print(prices[:3])
# print(prices[-3:])
# print(prices[2:5+1])
# print(prices[::-1])





# signals = ['BUY', 'SELL', 'BUY', 'WAIT', 'SELL', 'BUY', 'CANCEL', 'BUY']
# сol_buy = signals.count('BUY')
# col_sell = signals.count('SELL')
# sell_first = signals.index("SELL")
# if 'HOLD' in signals:
#     print('HOLD присутсвует')
# else:
#     print('Нет')
# new = []
# for i in signals:
#     if i == 'BUY' or i == 'SELL':
#         new.append(i)
# print(new)
# print(len(new))



# prices = [120, 85, 140, 95, 160, 110, 75]
# mx = prices[0]
# mn = prices[0]
# t_mx = 0
# t_mn = 0
# for i in range(0, len(prices)):
#     if prices[i] > mx:
#         mx = prices[i]
#         t_mx = i 
#     if prices[i] < mn:
#         mn = prices[i]
#         t_mn = i
# print(mn, mx )
# print(t_mn, t_mx)




# prices = [42000, 43500, 41000, 46000, 44500, 48000, 43000]
# col = 0
# mx = 0
# t_ind = 0

# for ind, value in enumerate(prices):
#     if value > 44_000:
#         print(f'Индекс: {ind}, Цена: {value}')
#         col += 1
#         if value > mx:
#             mx = value
#             t_ind = ind 
# print(col)
# print(t_ind)
# print(mx)




# prices = [100, 115, 110, 130, 125, 140, 135]
# higher = 0 
# lower = 0 
# mx = 0
# list_ind = [0,0]

# for i in range(0, len(prices)-1):
#     times = prices[i+1] - prices[i]
#     if times > mx:
#         mx = times
#         list_ind = [i, i+1]
#     if prices[i+1] > prices[i]:
#         higher += 1
#     if prices[i+1] < prices[i]:
#         lower += 1

# print(f'Повышений: {higher}')
# print(f'Падений: {lower}')
# print(f'Максимальное повышение: {mx}')
# print(f'Между индексами: {list_ind[0]} и {list_ind[1]}')





# prices = [100, 110, 120, 115, 125, 135, 140, 130]

# current = 0  
# best = 0

# start = 0       
# best_start = 0
# best_end = 0

# for i in range(len(prices) - 1):

#     if prices[i + 1] > prices[i]:
#         current += 1

#     else:
#         current = 0
#         start = i + 1

#     if current > best:
#         best = current
#         best_start = start
#         best_end = i + 1

# print(f'Максимальная серия: {best}')
# print(f'Начальный индекс: {best_start}')
# print(f'Конечный индекс: {best_end}')


# a = [10, 20, 30, 40, 50, 60]
# for i in range(0, len(a)-1, 2):
#     term = a[i]
#     a[i] = a[i+1]
#     a[i+1] = term
# print(a)


# a = [10, 20, 30, 40, 50, 60]

# for i in range(0, len(a)//2):
#     term = a[i]
#     a[i] = a[len(a)-1-i]
#     a[len(a)-1-i] = term 
# print(a)


# a = [3, 8, 5, 12, 7, 10, 4]
# i = 0
# while i < len(a):
#     if a[i] % 2 == 0:
#         a.pop(i)
#     else:
#         i += 1
# print(a)


# a = [2, 4, 6, 7]
# for i in range(len(a)-1, -1,-1):
#     if a[i] % 2 == 0:
#         a.pop(i)
# print(a)


# a = [5, 2, 4, 1]
# for i in range(0, len(a)-1):
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j+1]:
#             term = a[j]
#             a[j] = a[j+1]
#             a[j+1] = term
# print(a)


# a = [4, 7, 4, 2, 7, 9, 2, 5]
# result = []

# for i in range(0, len(a)):
#     if a[i] not in result:
#         result.append(a[i])
#     else:
#         continue
# print(result)
        



# a = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s += a[i][j]
# print(s)



# a = [
#     [4, 7, 2],
#     [9, 1],
#     [3, 8, 5, 6],
#     [10]
# ]
# res = []
# for i in range(len(a)):
#     s = 0 
#     for j in range(len(a[i])):
#         t = a[i][j]
#         s += t 
#     res.append(s)
# print(res)


# a = [7, -3, 12, 0, -8, 5, 12, -3, 9, 0, 4]
# res = []
# for i in range(len(a)):
#     if a[i] not in res and a[i] > 0:
#         res.append(a[i])
# print(res)








