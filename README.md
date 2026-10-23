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
