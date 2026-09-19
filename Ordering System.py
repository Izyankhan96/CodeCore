print("Welcome to the ordering system beta ")
food = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]
print("Here is the menu:")
print(food)
order = input("What would you like to order? ")
if order in food:
    print(f"Great choice! You have ordered {order}.")
else:
    print("Sorry, that item is not on the menu.")
drink = ["Water", "Soda", "Pineapple Fanta special", "Juice"]
print("Here are the available drinks:")
print(drink)
option_drink = input("What drink would you like to order? : ")
price_pizza = 10
price_burger = 8
price_pasta = 12
price_salad = 7
price_sushi = 15
if order == "Pizza":
    print(f"The price of your order is ${price_pizza}.")
elif order == "Burger":
    print(f"The price of your order is ${price_burger}.")
elif order == "Pasta":
    print(f"The price of your order is ${price_pasta}.")
elif order == "Salad":
    print(f"The price of your order is ${price_salad}.")
elif order == "Sushi":
    print(f"The price of your order is ${price_sushi}.")
price_water = 1
price_soda = 2
price_pineapple_fanta_special = 3
price_juice = 2
if option_drink == "Water":
    print(f"The price of your drink is ${price_water}.")
elif option_drink == "Soda":
    print(f"The price of your drink is ${price_soda}.")
elif option_drink == "Pineapple Fanta special":
    print(f"The price of your drink is ${price_pineapple_fanta_special}.")
elif option_drink == "Juice":
    print(f"The price of your drink is ${price_juice}.")
else:
    print("Sorry, that drink is not available.")

print("Your order summary:")
print(f"Food: {order}")
print(f"Drink: {option_drink}")

print("Thank you for your order! Your food will be ready shortly.")