# CodeCore

A small collection of Python practice projects.

## Guessing Game (no number edition)

A console word guessing game with difficulty levels, built using beginner
Python topics: variables, input, if/else, lists, while loops, `break` and the
`random` module.

- Pick a level: `Easy`, `Medium` or `Hard`. Each level has its own list of
  words.
- Guess the word. A wrong guess says so and lets you guess again.
- The secret word changes after every guess.
- Capital letters and extra spaces are ignored in guesses, so `white stone`
  counts as `White Stone`.
- Capital letters and extra spaces are ignored in the level too, so ` easy `
  works. Anything else asks again.

### Running it

```
python3 "Guessing Game.py"
```

## Password Generator

A console password generator with difficulty levels, built using beginner
Python topics: variables, input, if/elif/else, lists, strings, while loops,
f-strings and the `random` module.

- Pick a level. Capital letters and extra spaces are ignored, so ` easy `
  works. Anything else asks again.
- `Easy` makes an 8-character password from capital letters.
- `Medium` makes a 12-character password from capital letters and numbers.
- `Hard` makes a 16-character password from lowercase and capital letters,
  numbers and the symbols `!@#$`.

### Running it

```
python3 "Password generator.py"
```

## Other projects

The ATM project used to live on this branch. It can still be found in the git
history.
