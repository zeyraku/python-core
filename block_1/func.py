# def calculate_balance(income, expense):
#     balance = income - expense

#     if balance < 0:
#         return "Недостаточно средств"

#     return balance

# result = calculate_balance(3000, 5000)
# print(result)

# result = calculate_balance(10000, 4000)
# print(result)


# def withdraw(balance, amount):
#     if amount > balance:
#         return('Недостаточно средств')
#     elif amount <= 0: 
#         return('Некорректная сумма')
#     else:
#         return balance - amount 
# first = withdraw(5000,6000)
# print(first)


# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result * 2)





# price = 2000
# quantity = 3
# discount = 10
# delivery = 300

# def calcuate_total(price, quantity):
#     return price * quantity

# def apply_discount(total, discount):
#     return total - (total * (discount / 100))

# def calcuate_price(discounted_total, delivery):
#     return discounted_total + delivery

# total = calcuate_total(price, quantity)
# discount_price = apply_discount(total, discount)
# final = calcuate_price(discount_price, delivery)
# print(f"Стоимость с учётом скидки: {final}")



# def calcuate_salary(hours, rate, bonus=0):
#     salary = (hours*rate) + bonus
#     return salary 

# print(calcuate_salary(5, 700, 20))
# print(calcuate_salary(bonus=2000, rate = 500, hours = 30))






# def deposit(balance, amount):
#     new_balance = balance + amount
#     return new_balance 

# def withdraw(balance, amount):
#     if amount > balance:
#         print('Недостаточно средств')
#         return balance 
#     return balance - amount

# def show_balance(balance):
#     print(balance )

# balance = 10_000 
# print(deposit(balance, 2000))
# show_balance(balance)



# def create_user(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# create_user(name="Alex", age=20, city="Moscow")





# def deposit(balance: int, amount: int) -> int:
#     return balance + amount

# def withdraw(balance: int, amount: int) -> int:
#     if amount <= 0:
#         print("Неправильная сумма")
#         return balance

#     if amount > balance:
#         print("Недостаточно средств")
#         return balance

#     return balance - amount

# def show_balance(balance:int) -> None:
#     print(f"Баланс: {balance}")



# def recurs(n):
#     if n == 0:
#         print('Конец')
#         return 
#     else:
#         print(n)
#         recurs(n-1)
# recurs(6)





# students = [
#     {"name": "Алексей", "scores": [80, 90, 70]},
#     {"name": "Мария", "scores": [95, 100, 90]},
#     {"name": "Иван", "scores": [40, 50, 45]},
#     {"name": "Анна", "scores": [75, 85, 80]}
# ]


# def calculate_grades(scores: list[int]) -> float:
#     total = 0 
#     for score in scores:
#         total += score
#     avg = total / len(scores)
#     return avg


# def check_status(student_avg_grade: float) -> str:
#     if student_avg_grade >= 60:
#         return 'Сдал'
#     else:
#         return 'Не сдал'


# def process_students(students) -> None:
#     for student in students:
#         avg = calculate_grades(student["scores"])
#         status = check_status(avg)

#         print(f"{student['name']}: {avg} | {status}")
    

# process_students(students)




# orders = [
#     {"id": 1, "customer": "Алексей", "items": [1200, 800, 500]},
#     {"id": 2, "customer": "Мария", "items": [3000, 1500]},
#     {"id": 3, "customer": "Иван", "items": [400, 300]},
#     {"id": 4, "customer": "Анна", "items": [2500, 2000, 1000]}
# ]

# def calculate_total_items(prices: list[int]) -> int:
#     return sum(prices)

# def get_discount(total: int) -> float:
#     if total >= 5000:
#         disc = 10 
#         return total * (disc/100)
#     elif total >= 2000:
#         disc = 5 
#         return total * (disc/100)
#     else:
#         return 0 

# def process_order(orders) -> None:
#     for request in orders:
#         one_req = request['items']
#         summa_request = calculate_total_items(one_req)
#         discount = get_discount(summa_request)

#         print(f"{request['customer']}: сумма {summa_request} ₽ | скидка {discount} ₽ | итог {summa_request - discount}")

# process_order(orders)




# players = [
#     {"name": "Воин", "health": 85, "damage": [20, 25, 30]},
#     {"name": "Маг", "health": 45, "damage": [40, 50, 60]},
#     {"name": "Лучник", "health": 70, "damage": [25, 35, 30]},
#     {"name": "Танк", "health": 100, "damage": [10, 15, 20]}
# ]

# def calculate_damage(damage: list[int]) -> int:
#     total = 0 
#     for harm in damage:
#         total += harm 
#     return total 

# def analyze_player(info_player: dict) -> dict:
#     total_damage = calculate_damage(info_player['damage'])

#     status = None 
#     if info_player['health'] > 50:
#         status = 'Жив'
#     else:
#         status = 'Ранен'

#     each_player = {
#         "name": info_player['name'],
#         "total_damage": total_damage,
#         "status": status
#     }
#     return each_player

# def process_player(players) -> None:
#     for i in players:
#         dict_player = analyze_player(i)
#         print(f"Имя игрока: {dict_player['name']} | урон: {dict_player['total_damage']} | статус: {dict_player['status']}")
        


# process_player(players)







