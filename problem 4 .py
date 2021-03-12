#Jordan Kendall
#2/26/21
#CSS 225

# it's telling us to write a program if it's divisible by 5,3 or both
for number in range(1,51):


    if number % 5 == 0 and number % 3 == 0:
        print("Divisible by both")
    elif number%3 == 0:
        print("Divisible by 3")
    elif number%5 == 0:
        print("Divisible by 5")
    else:
        print(number)



