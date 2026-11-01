# student = {
#     "name": "ALex",
#     "age": 19,
#     "language": "Python"
# }
# print(student)


# user = {
#     "name": "Alex",
#     "age": 19,
#     "city": "Moscow"
# }

# user["age"] = 20 
# user["language"] = "Python"
# user["city"] = 'Kazan'
# print(user)



# product = {
#     "name": "Laptop",
#     "price": 75000,
#     "quantity": 5,
#     "category": "Electronics"
# }

# del product["category"]
# removed_quantity = product.pop("quantity", None)
# print(removed_quantity)
# print(product)



# user = {
#     "name": "Max",
#     "age": 21,
#     "email": "max@example.com"
# }

# if 'email' in user:
#     print(user["email"])
# else:
#     print(None)

# if 'phone' in user:
#     print(user['phone'])
# else:
#     print(None)


# profile = {
#     "username": "python_dev",
#     "level": 5,
#     "city": "Moscow"
# }

# print(profile.get("username"))
# print(profile.get("level"))
# print(profile.get("phone", 'Телефон не указан'))
# print(profile.get("country", 'Страна неизвестна'))



# stock = {
#     "keyboard": 12,
#     "mouse": 8,
#     "monitor": 4,
#     "headphones": 6
# }

# total = 0
# for key, value in stock.items():
#     total += value
#     print(f"{key}: {value} шт.")
# print(total)



# languages = ["Python", "Java", "Python", "C++", "Java", "Python"]
# counts = {

# }

# for lang in languages:
#     if lang not in counts:
#         counts[lang] = 1
#     else:
#         counts[lang] += 1
# for key, value in counts.items():
#     print(f"{key:<10} | {value:>6}")





# users = {
#     "alex": {
#         "age": 19,
#         "city": "Moscow"
#     },
#     "max": {
#         "age": 21,
#         "city": "Kazan"
#     }
# }

# print(users["alex"]["age"])
# print(users["max"].get("country", 'Не указана'))
# users["max"]["age"] = 22 
# users["alex"]["language"] = "Python"
# print(users["max"].get("city", 'Не указан'))

# for username, info in users.items():
#     print(f"Пользователь: {username}")

#     for field, value in info.items():
#         print(f"  {field}: {value}")



# products = [
#     {"name": "Keyboard", "price": 3500},
#     {"name": "Mouse", "price": 1500},
#     {"name": "Monitor", "price": 18000}
# ]

# total = 0 
# for product in products:
#     total += product["price"]
#     print(f"{product["name"]} | {product['price']}")
# print(total)



# numbers = [2, 3, 4, 5, 6]
# cubes = {
#     element: element ** 3 for element in numbers
# }
# for key, value in cubes.items():
#     print(f"{key} | {value}")





# orders = [
#     {"user": "Alex", "product": "Keyboard", "price": 3500},
#     {"user": "Max", "product": "Mouse", "price": 1500},
#     {"user": "Alex", "product": "Monitor", "price": 18000},
#     {"user": "Anna", "product": "Mouse", "price": 1500},
#     {"user": "Max", "product": "Keyboard", "price": 3500},
#     {"user": "Alex", "product": "Mouse", "price": 1500}
# ]

# user_totals = {

# }
# for order in orders:
#     if order["user"] not in user_totals:
#         user_totals[ order["user"]  ] = order["price"]    # словарь ордер -> ключ user -> значение user
#     else:
#         user_totals[ order["user"]  ] += order["price"]

# for key, value in user_totals.items():
#     print(f"{key}: | {value}")





# orders = [
#     {"user": "Alex", "category": "Electronics", "price": 3500},
#     {"user": "Max", "category": "Books", "price": 1200},
#     {"user": "Anna", "category": "Electronics", "price": 18000},
#     {"user": "Alex", "category": "Books", "price": 800},
#     {"user": "Max", "category": "Electronics", "price": 1500},
#     {"user": "Anna", "category": "Books", "price": 600}
# ]

# mx = 0 
# max_category = None

# tovs = {

# }
# for good in orders:
#     if good["category"] not in tovs:
#         tovs[ good["category"] ] = good["price"]
#     else:
#         tovs[ good["category"] ] += good["price"]


# for key, value in tovs.items():
#     if value > mx: 
#         max_category = key 
#         mx = value 
#     else:
#         continue
# print(f"Категория с самой высокой стоимостью: {max_category}")
# print(f"Её стоимость: {mx}")













