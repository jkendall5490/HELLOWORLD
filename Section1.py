#Jordan Kendall
#2/3/2021
#CSS 225
from Main_Character import player
def start():
    print("Welcome to My Game")
    print("Car Trouble")
    print("Jordan's having car trouble and can't get it to fix")
    choice =input (" A: Tow Truck B:Police C:Fire ")
    if choice =='A':
        print("If Jordan calls a tow tow truck he gets help from Tow Truck service to tow his car to the nearest auto repair")
        print("He also tells them his vehicle location and he moves on to section 2")
        if player.Money >5000:
           player.Money=player.Money-5000
           return
        #elif player.Money<5000

        #Later I add the code to move to Section 2
    elif choice == 'B':
        print("If he calls the police the police wouldn't know how to tell the person what do in the car trouble scenario that he's in")
        print("he doesn't get a response from them")
        # If the player choose B it's game over
    elif choice == 'C':
        print("if he calls the fire department they won't know what to tell him and explain only use this number for extreme emergencies ")
        print("He doesn't get a response either from the fire department")

    #Car Trouble
    #Jordan’s car stopped on the expressway and cant get it to fix
    #Call a tow truck  ; call the police; calling the fire department ; Use coins to pay the tow truck service people.
    #if he calls the tow truck then he tell him his location of his vehicle and he moves on to section 2
    #if he calls the police he doesn't get any response from them ; he makes another call
    #if he calls the fire department he doesn't get any respone either; and that's game over
    #he uses trhe coins to pay the tow truck service back for towing his car ; if cost 50 coins