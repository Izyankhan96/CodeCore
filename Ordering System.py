print("Welcome to the ordering system beta ")
food = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]
print("Here is the menu:")
for item in food:
    print(f"- {item}")
order = input("What would you like to order? ").strip().title()
while order not in food:
    print("Sorry, that item is not on the menu. Please try again.")
    order = input("What would you like to order? ").strip().title()
print(f"Great choice! You have ordered {order}.")
drink = ["Water", "Soda", "Pineapple Fanta Special", "Juice"]
print("Here are the available drinks:")
for item in drink:
    print(f"- {item}")
option_drink = input("What drink would you like to order? : ").strip().title()
while option_drink not in drink:
    print("Sorry, that drink is not available. Please try again.")
    option_drink = input("What drink would you like to order? : ").strip().title()
price_pizza = 10
price_burger = 8
price_pasta = 12
price_salad = 7
price_sushi = 15
if order == "Pizza":
    food_price = price_pizza
elif order == "Burger":
    food_price = price_burger
elif order == "Pasta":
    food_price = price_pasta
elif order == "Salad":
    food_price = price_salad
elif order == "Sushi":
    food_price = price_sushi
print(f"The price of your order is ${food_price}.")
price_water = 1
price_soda = 2
price_pineapple_fanta_special = 3
price_juice = 2
if option_drink == "Water":
    drink_price = price_water
elif option_drink == "Soda":
    drink_price = price_soda
elif option_drink == "Pineapple Fanta Special":
    drink_price = price_pineapple_fanta_special
elif option_drink == "Juice":
    drink_price = price_juice
print(f"The price of your drink is ${drink_price}.")

total = food_price + drink_price

print("Your order summary:")
print(f"Food: {order} - ${food_price}")
print(f"Drink: {option_drink} - ${drink_price}")
print(f"Total: ${total}")

print("Thank you for your order! Your food will be ready shortly.")
