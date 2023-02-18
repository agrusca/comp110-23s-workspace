"""EX03 - Wordle."""

__author__ = "730309157"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(str_input: str, single_character: str) -> bool:
    """Checks whether single_character is found at any index of str_input."""
    assert len(single_character) == 1
    current_idx: int = 0
    does_character_exist: bool = False
    while does_character_exist is False and current_idx < len(str_input):
        #  while single_character has not been found at any index of str_input and the index is less than length of str_input
        if str_input[current_idx] == single_character:
            #  if str_input at the current index equals single_character
            does_character_exist = True
        current_idx = current_idx + 1 
    return does_character_exist


def emojified(guess: str, secret: str) -> str: 
    """Codifies characters in guess depending on whether they exist in secret."""
    assert len(guess) == len(secret)
    current_idx: int = 0
    resulting_emoji: str = ""
    while current_idx < len(secret):
        if guess[current_idx] == secret[current_idx]:
            #  if specific index of guess matches specific index of secret word
            resulting_emoji = resulting_emoji + GREEN_BOX
        else: 
            #  if specific index of guess does NOT match index of secret word
            if contains_char(secret, guess[current_idx]) is True:
                # if any index of guess exists in secret
                resulting_emoji = resulting_emoji + YELLOW_BOX
            else: #  if any index of guess does not exist in secret
                resulting_emoji = resulting_emoji + WHITE_BOX
        current_idx = current_idx + 1  
    return resulting_emoji


def input_guess(expected_length: int) -> str:
    """Prompts user for guess of length expected_length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        # while the length of guess is not equal to the expected length 
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1
    game_won: bool = False
    guess: str = ""
    while turns < 7 and game_won is False:
        #  while user has not exceeded 6 turns and the game has not been won
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        #  assigns user guess to input of being asked for word that matches the length of secret
        print(emojified(guess, secret))
        #  prints emojis to tell user which letters match those of the secret and whether they are at the same index
        if guess == secret:
            game_won = True
            print(f"You won in {turns}/6 turns!")
        if turns == 6 and game_won == False:
            print("X/6 - Sorry, try again tomorrow!")
        turns = turns + 1


if __name__ == "__main__":
    main()