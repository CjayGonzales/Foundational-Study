# place in a 6 letter word
# any word with a "0" in the title will generate letters from a - z
# will need to account for words that are already guessed to exclude
# return a list of potential letters in place of 0

# need to store the position of the 0
# need to print it out a lot nicer but progress!

def guessWord():
    letterList = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    word = input()
    if len(word) > 6:
        print("Your word is too long dummy")
        return
    else:
        for letter in word:
            if letter == "0":
                for x in letterList:
                    
                    print(x)
            else:
                print(letter)

    # print(word)

guessWord()