"""EX02 - One shot wordle."""

__author__ = "730309157"

secret_word: str = ("python")
original_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
current_index: int = 0
resulting_emoji: str = ("")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(original_guess) != len(secret_word):
    # if guess is not correct length 
    new_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")
    original_guess = new_guess
if len(original_guess) == len(secret_word):
    # if guess is correct length 
    while current_index < len(secret_word):
        if original_guess[current_index] == secret_word[current_index]:
            # if specific index of guess matches specific index of secret word
            resulting_emoji = resulting_emoji + GREEN_BOX
        else: 
            # if specific index of guess does NOT match index of secret word
            does_character_exist: bool = False 
            alternate_index: int = 0
            while does_character_exist is False and alternate_index < len(secret_word):
                if secret_word[alternate_index] == original_guess[current_index]:
                    # if character in secret word at certain index matches any of the characters in guess at different index 
                    does_character_exist = True
                alternate_index = alternate_index + 1 
            if does_character_exist is True:
                resulting_emoji = resulting_emoji + YELLOW_BOX
            else:
                resulting_emoji = resulting_emoji + WHITE_BOX
        current_index = current_index + 1
    print(resulting_emoji)
    if original_guess == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")