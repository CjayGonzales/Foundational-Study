def inputChecker():
    print("Please enter string you wish to check")
    stringToCheck = input()

    if stringToCheck == "":
        print("Please enter a value")
        return

    print("please enter character you wish to find")
    chrToFind = input()
    n = 0

    for item in chrToFind:
        n = n + 1
    if n > 1:
        print("Please enter only one character")
        return
    else:
        myArr = []
        for x in stringToCheck:

            myArr.append(x)
            # print(myArr)

        if chrToFind in myArr:
            print("Found the character you wanted to find!: " + chrToFind)
        else:
            print("Could not find the character you wanted!")
            return

inputChecker()