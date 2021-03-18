#Jordan Kendall
#2/3/2021
#CSS 225
from Main_Character import player
def start():
    print("Level 2")
    print("player name is Jordan")
    print("Jordan is trying to get to a party but gets lost pretty easily")
    def gochoice():
        choice=input("A.Go to a nearby restaurant B.Use a GPS .C Ask somebody for directions")
        return choice
    choice = gochoice()
    while  "GPS" not in player.Inventory:
        if choice =="A":
            print("If Jordan goes to a nearby restaurant and meets some friends he knows that are going to the party ")

            player.Inventory.append("Map")
            player.Inventory.append("GPS")
            print(player.Inventory)
            choice = gochoice()
        elif choice == "B":
            print("If Jordan uses a GPS he will automacailly get to the party faster ")
            if "GPS" not in player.Inventory:
                print("Jordan doesn't have a GPS, he needs to find one!")
                print(player.Inventory)
                choice = gochoice()
            else:
                player.Inventory.append("Car")
                player.Inventory.append("Navigator")
                print(player.Inventory)
        elif choice == "C":
            print("If you ask someone for directions you go to Section 3")
            return
            choice = gochoice()
        else:
            print("invalid input")
            choice = gochoice()

#Getting to a party
#Jordan and her friends are driving to a party but got lost very easily and can't find the party location
#Go to nearby restaurant; Ask someone nearby for directions; use a gps on your phone for the location ; call on of your friends on your friends list at the party; Using Coins for when we arrived at a gas station
# if he goes to a nearby restaurant he cancels going over to the party
#if Jordan  ask for someone for nearby directions it's game over
#if Jordan  uses his  gps on his phone for the location she goes to section 3
#if Jordan call one of his friends on his friends list she gets to the party
