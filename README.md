# CodeCore

A small collection of Python practice projects.

## ATM

A simple console ATM for FDB Bank, built using only beginner Python topics:
variables, input, f-strings, if/elif/else, lists and while loops.

- Enter the PIN to log in (it keeps asking until the PIN is correct).
- Pick an option from the menu: 1 Withdrawal, 2 Deposit, 3 Balance Inquiry,
  4 Exit.
- Withdrawals must be more than $0, no more than $1000 at a time, and no more
  than your balance.
- Amounts must be whole dollars typed with numbers only (e.g. `50`). Anything
  else, such as `abc`, `20.50`, `$50` or a blank entry, asks for the amount
  again.

### Running it

```
python3 ATM.py
```

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
