#Jordan Kendall
#CSS 225
#3/17/2021
import random
Score=0
GreenArrow=10
scorecard = []
while GreenArrow >= 1:
    score = random.randint(0,10)
    #list.append(value)
    scorecard.append(score)
    if score == 10:
        #Score = Score + 20
        Score += 20
        GreenArrow -= 1
        print("You got a bullseye!")
    elif score == 0:
        Score += 0
        GreenArrow += 0
        print("You missed!")
    else:
        Score += score
        GreenArrow -= 1
print("Final Score: ", Score)
print("Final Scorecard",scorecard)
print("Congrats you win the game")