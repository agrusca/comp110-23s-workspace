"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730309157"

five_letter_word: str = input("Enter a 5-character word: ")
if (len(five_letter_word) != 5):
    exit(print("Error: Word must contain 5 characters"))
single_character: str = input("Enter a single character: ")
if (len(single_character) != 1):
    exit(print("Error: Character must be a single character."))
number_of_matching_characters: int = 0 

print("Searching for " + single_character + " in " + five_letter_word)
if (five_letter_word[0] == single_character):
    print(single_character + " found at index 0 ") 
    number_of_matching_characters = number_of_matching_characters + 1 
if (five_letter_word[1] == single_character):
    print(single_character + " found at index 1 ")
    number_of_matching_characters = number_of_matching_characters + 1 
if (five_letter_word[2] == single_character):
    print(single_character + " found at index 2 ")
    number_of_matching_characters = number_of_matching_characters + 1 
if (five_letter_word[3] == single_character):
    print(single_character + " found at index 3 ")
    number_of_matching_characters = number_of_matching_characters + 1 
if (five_letter_word[4] == single_character):
    print(single_character + " found at index 4 ")
    number_of_matching_characters = number_of_matching_characters + 1 

if (number_of_matching_characters == 0):
    print("No instances of " + single_character + " found in " + five_letter_word)
if (number_of_matching_characters == 1):
    print("1 instance of " + single_character + " found in " + five_letter_word)
if (number_of_matching_characters == 2):
    print("2 instances of " + single_character + " found in " + five_letter_word)
if (number_of_matching_characters == 3):
    print("3 instances of " + single_character + " found in " + five_letter_word)
if (number_of_matching_characters == 4):
    print("4 instances of " + single_character + " found in " + five_letter_word)
if (number_of_matching_characters == 5):
    print("5 instances of " + single_character + " found in " + five_letter_word)