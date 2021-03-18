#Jordan Kendall
#2/3/2021
#CSS 225

def start():
    print("Level 3")
    print("player name is jordan")
    print("Jordan and his friends are tying to get to a concert but ran out of gas")
    def gochoice():
        choice=input("A.Push car to gas station .B Call the police C. Call friends for directions ")
        return choice
    choice = gochoice()
    if choice == "C":
        print("if Jordan calls friends for directions it's game over")
        exit()
    if   choice  ==  "B":
        print("If Jordan calls the police he basically gets no service ")
    elif choice =="A":
            print("if Jordan pushes car to gas station he wins the game ")

            return
            choice=gochoice()
#Getting to a concert
#Jordan  and his friends are driving to a concert and ran out a gas in a nearby nieghborhood
#Push the car to the gas station; call tow truck ; call police.Call your friends on your friends list for directions; using coins to buy passes to arrive earlier or later
#if he chooses Push the car to the gas station it's game over
#if he call the police they won't respond
#if he call his friends for direction he passes on to section 4
#if he has coins he could buy the passes to arrive earlier or later


