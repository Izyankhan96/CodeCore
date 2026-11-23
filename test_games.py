"""Tests for GuessingGame.py and PasswordGenerator.py.

The games run straight away when Python opens them, and they ask the
player for input. So each test:

  1. pretends to be the player, by replacing input() with a list of
     answers typed in advance,
  2. runs the game file with runpy, and
  3. catches everything the game prints, so we can check it.

For the guessing game we also choose the "random" word ourselves, so the
test knows what the right answer is.

Run all tests with:   python3 -m unittest -v
"""

import io
import os
import runpy
import string
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


# The folder this test file lives in, so the games are found from anywhere.
HERE = os.path.dirname(os.path.abspath(__file__))


def play(game_file, answers, secret_word=None):
    """Run a game file with typed answers and return what it printed.

    answers:      the things the player types, in order.
    secret_word:  if given, random.choice always picks this word.
    """
    game_file = os.path.join(HERE, game_file)
    output = io.StringIO()
    with patch("builtins.input", side_effect=answers):
        with redirect_stdout(output):
            if secret_word is None:
                runpy.run_path(game_file)
            else:
                with patch("random.choice", return_value=secret_word):
                    runpy.run_path(game_file)
    return output.getvalue()


class TestGuessingGame(unittest.TestCase):

    def test_easy_right_guess_wins(self):
        printed = play("GuessingGame.py", ["Easy", "Gate"], secret_word="Gate")
        self.assertIn("You guessed it!", printed)

    def test_medium_right_guess_wins(self):
        printed = play("GuessingGame.py", ["Medium", "Win"], secret_word="Win")
        self.assertIn("You guessed it!", printed)

    def test_hard_right_guess_wins(self):
        printed = play("GuessingGame.py", ["Hard", "Lol"], secret_word="Lol")
        self.assertIn("You guessed it!", printed)

    def test_capitals_and_spaces_ignored_in_guess(self):
        printed = play("GuessingGame.py", ["Easy", "  wHITE sTONE "],
                       secret_word="White Stone")
        self.assertIn("You guessed it!", printed)

    def test_capitals_and_spaces_ignored_in_level(self):
        printed = play("GuessingGame.py", ["  hARD ", "Haha"],
                       secret_word="Haha")
        self.assertIn("Okay............", printed)
        self.assertIn("You guessed it!", printed)

    def test_wrong_guess_lets_you_try_again(self):
        printed = play("GuessingGame.py", ["Easy", "Banana", "Gate"],
                       secret_word="Gate")
        self.assertIn("Wrong try again!", printed)
        self.assertIn("You guessed it!", printed)

    def test_bad_level_asks_again(self):
        printed = play("GuessingGame.py", ["Super hard", "Easy", "Gate"],
                       secret_word="Gate")
        self.assertIn("Not a valid level", printed)
        self.assertIn("You guessed it!", printed)


class TestPasswordGenerator(unittest.TestCase):

    def get_password(self, answers):
        """Run the generator and pull the password out of what it printed."""
        printed = play("PasswordGenerator.py", answers)
        for line in printed.splitlines():
            if line.startswith("Your password is: "):
                return line[len("Your password is: "):]
        self.fail("The generator never printed a password")

    def test_easy_password(self):
        password = self.get_password(["Easy"])
        self.assertEqual(len(password), 8)
        for letter in password:
            self.assertIn(letter, "ABCDEFGHIJKL")

    def test_medium_password(self):
        password = self.get_password(["Medium"])
        self.assertEqual(len(password), 12)
        for letter in password:
            self.assertIn(letter, string.ascii_uppercase + "123")

    def test_hard_password(self):
        password = self.get_password(["Hard"])
        self.assertEqual(len(password), 16)
        allowed = string.ascii_lowercase + "ABCDEFGHJKL12345!@#$"
        for letter in password:
            self.assertIn(letter, allowed)

    def test_capitals_and_spaces_ignored_in_level(self):
        password = self.get_password(["  mEDIUM "])
        self.assertEqual(len(password), 12)

    def test_bad_level_asks_again(self):
        printed = play("PasswordGenerator.py", ["Impossible", "Easy"])
        self.assertIn("That's not a level", printed)
        self.assertIn("Your password is: ", printed)


if __name__ == "__main__":
    unittest.main()
