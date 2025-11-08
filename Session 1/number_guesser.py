import random

def numberGuesser():
    print("Hello, welcome to the random number guesser! Please guess a number from the range of 1 - 100")
    
    random_num = random.randrange(0, 100)
    chances = 5

    while chances > 0:
        user_guess = input()
        print("Your guess:" + user_guess)

        if int(user_guess) == random_num:
            print("You guessed correctly!")
            return
        else:
            print("Incorrect guess!")
            print("You have: " + str(chances - 1 ) + " chances left")
            print(random_num)
            chances = chances -1

numberGuesser()