# CodeCore

A small collection of Python practice projects.

## Ordering System

A command line ordering system. It shows a food menu and a drink menu,
asks what you want, and prints a receipt with the total.

### Running it

```
python3 "Ordering System.py"
```

Requires Python 3.6 or newer (it uses f-strings). No dependencies to
install.

### Menu

| Food   | Price | Drink                   | Price |
| ------ | ----- | ----------------------- | ----- |
| Pizza  | $10   | Water                   | $1    |
| Burger | $8    | Soda                    | $2    |
| Pasta  | $12   | Pineapple Fanta Special | $3    |
| Salad  | $7    | Juice                   | $2    |
| Sushi  | $15   |                         |       |

### Notes

Input is not case sensitive and surrounding spaces are ignored, so
`  pizza ` is read as `Pizza`. Anything that is not on the menu is
rejected and asked for again.

### Example

```
Here is the menu:
- Pizza
- Burger
- Pasta
- Salad
- Sushi
What would you like to order? sushi
Great choice! You have ordered Sushi.
...
Your order summary:
Food: Sushi - $15
Drink: Juice - $2
Total: $17
```
