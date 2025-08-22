import random, time

card_names = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Hearts","Diamonds","Spades","Clubs"]
deck_of_cards = []
points = 0 

value = 1
for rank in card_names:
    for suit in suits:
        deck_of_cards.append([rank + " of " + suit, value])
    value = value + 1

random.shuffle(deck_of_cards)


points = 0
play = input("Would you like to play? [play] or [exit]: ")

if play[0].lower() == "p":
    print("The aim of the game is to correctly guess whether a card will be higher or lower than the previous. Score points by consecutively guessing correctly")
    while True:
        card0 = deck_of_cards.pop(0)
        print(f"\n\nYour current points are: {points}")
        print(f"\nThe card is {card0[0]}")
        while True:
            choice = input("Higher or lower? ")
            time.sleep(2)
            if len(choice) > 0:
                if choice[0].lower() in["l","h"]:
                    break
        
        card1 = deck_of_cards.pop(0)
        print(f"\nThe card is {card1[0]}\n")
        time.sleep(3)

        if choice[0].lower() == "h" and card0[1] > card1[1]:
            print(f"Incorrect {card1[0]} is not higher than {card0[0]}")
            print(f"You finished with a total of {points} points!")
            points = 0
            time.sleep(1)
            break
        elif choice[0].lower() == "h" and card0[1] < card1[1]:
            print(f"Correct {card1[0]} is higher than {card0[0]}")
            points += 1
            time.sleep(1)
        elif choice[0].lower() == "l" and card0[1] > card1[1]:
            print(f"Correct {card1[0]} is lower than {card0[0]}")
            points += 1
            time.sleep(1)
        elif choice[0].lower() == "l" and card0[1] < card1[1]:
            print(f"Incorrect {card1[0]} is not lower than {card0[0]}")
            print(f"You finished with a total of {points} points!")
            points = 0
            time.sleep(1)
            break
        else:
            print("DRAW")
else:
    print("Thanks for playing!")
