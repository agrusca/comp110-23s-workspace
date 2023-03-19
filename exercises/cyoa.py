"""Create your own adventure."""

__author__ = "730309157"

CAT: str = "\U0001F408"
CRYING_FACE: str = "\U0001F622"
PARTY_POPPER: str = "\U0001F389"
FISH: str = "\U0001F41F"
ANGRY_FACE: str = "\U0001F620"
ANNOYED_FACE: str = "\U0001F612"
NAUSEA_FACE: str = "\U0001F922"
ROLLING_EYES: str = "\U0001F644"
BLUSH_FACE: str = "\U0001F60A"
DISSAPOINTED_FACE: str = "\U0001F61E"

from random import randint

player: str = ""
points: int = 0

def greet():
    print(f"Welcome! Your friend Steve is going on vacation and has asked you to take care of their cat Meow {CAT}")
    global player
    player = input("What is your name? ")
    print(f"Awe, what a lovely name, {player}! {BLUSH_FACE}")

def main():
    global points
    greet()
    playing: bool = True
    while playing is True:
      print("Meow needs two things to remain a happy, healthy, and cheeky cat: food and play. Every interaction with Meow increases your points, and more points means a happier Meow!")
      if points == 0 or points > 1:
         print(f"You currently have {points} points, {player}.")
      else:
         print(f"You currently have {points} point, {player}.")
      accepted_choice: bool = False
      while accepted_choice is False:
        decision: str = input("Would you like to feed Meow, play with Meow, or go home and leave Meow to fend for himself? Type feed, play, or leave. ")
        if decision.lower() == "feed":
          accepted_choice = True
          feed()
        elif decision.lower() == "play":
          accepted_choice = True
          points = play(points)
          if points == 0 or points > 1:
             print(f"You now have {points} points.")
          else:
             print(f"You now have {points} point.")
        elif decision.lower() == "leave":
          accepted_choice = True
          exit_game()
          playing = False
        else:
          print("Your input didn't match any of the choices. Please try again.")
    
def exit_game():
   decision: str = input(f"Are you sure you want to leave Meow all alone? {CRYING_FACE} Type y if yes. ")
   if decision == "y":
      print(f"Thank you for taking care of Meow for Steve, {player}! Your score was {points} points.")
   
def play(point_amount: int) -> int:
   """Increases points variable based on playing interactions."""
   print("Yay! Its time to play!")
   play_points: int = 0
   accepted_toy: bool = False
   while accepted_toy is False:
    toy_choice: str = input("Would you like to bring out the laser, the ball, or the yarn? Type laser, ball, or yarn. ")
    if toy_choice.lower() == "laser":
       print(f"Yay! That's Meow's favorite toy {PARTY_POPPER} Great choice, {player}! You have earned 5 points!")
       play_points += 5
       accepted_toy = True
    elif toy_choice.lower() == "ball":
       print(f"That will keep Meow interested for a little bit, {player}, but that's not his favorite toy {ANNOYED_FACE} You have earned 3 points.")
       play_points += 3
       accepted_toy = True
    elif toy_choice.lower() == "yarn":
       print(f"Meow hates this toy! It gives him anger issues {ANGRY_FACE} Maybe you'll do better next time, {player}. Here is a point for trying.")
       play_points += 1
       accepted_toy = True
    else:
       print("Your input didn't match any of the choices. Please try again.")
   return point_amount + play_points
    
def feed():
   """Increases points variable based on feeding interactions"""
   global points
   print("Whew! Meow was very hungry. Steve shares cat food with his neighbor (who hates Meow and won't take care of him), so we never know how much of anything he'll have!")
   accepted_food: bool = False
   tuna_amount: int = randint(0,3)
   chicken_amount: int = randint(0,3)
   kibble_amount: int = randint(0,3)
   while accepted_food is False:
    food_choice: str = input(f"You have {tuna_amount} tuna, {chicken_amount} chicken, and {kibble_amount} kibble. What would you like to feed Meow? Type tuna, chicken, or kibble. ")
    if food_choice.lower() == "tuna": 
       if tuna_amount > 0:
          print(f"Mmmmm. Tuna {FISH} Meow loveeees tuna. Great choice, {player}. You have earned 5 points!")
          points += 5
          accepted_food = True
       else:
          print(f"You have no tuna, {player} {DISSAPOINTED_FACE} Please try again.")
    elif food_choice.lower() == "chicken":
       if chicken_amount > 0:
        print(f"Meow used to love chicken until it made him sick one time {NAUSEA_FACE}. Don't you remember Steve telling you about the mess he had to clean up, {player}? Hopefully he can keep it down this time. You have earned 3 points.")
        points += 3
        accepted_food = True
       else:
          print(f"You have no chicken, {player} {DISSAPOINTED_FACE} Please try again.")
    elif food_choice.lower() == "kibble":
       if kibble_amount > 0:
        print(f"Meow thinks kibble is peasant food {ROLLING_EYES} but if he's as hungry as he claims, he'll make do! At least you tried, {player}. You have earned one point.")
        points += 1
        accepted_food = True
       else:
          print(f"You have no kibble, {player} {DISSAPOINTED_FACE} Please try again.")
    else:
       print("Your input didn't match any of the choices. Please try again.")

if __name__ == "__main__":
  main()