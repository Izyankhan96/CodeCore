# CodeCore

A clean slate. The repository previously held scratch code for practising
test cases; that work has been removed and new project work starts here.

## Branch: `code-core-database`

This branch is reserved for future work and will continue to be developed
over time. New features and project code will be built here before being
merged elsewhere.

## Projects

### ATM (`ATM.py`)

A simple console ATM for FDB Bank, built using only beginner Python topics:
variables, input, f-strings, if/elif/else, lists and while loops.

- Enter the PIN to log in (it keeps asking until the PIN is correct).
- Pick an option from the menu: 1 Withdrawal, 2 Deposit, 3 Balance Inquiry,
  4 Exit.
- Withdrawals must be more than $0, no more than $1000 at a time, and no more
  than your balance.

Run it with:

```
python3 ATM.py
```

Typing letters when asked for an amount will crash the program. Handling that
needs `try`/`except`, which is a later topic.
