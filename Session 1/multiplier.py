# number multiplier
# create a function that takes in a parameter of a given number and multiples that until 12

# define the function
# take in a parameter
# use the parameter to print itself out until 12

# check to see if the value is greater than 12
# if it is return
# make a loop which adds upon itself until 12



def multiplier(x):
    if x > 12:
        print("Number is too big!")
        return
    
    i = 0
    while i <= 12:
        
        multiplied_value = i*x

        i = i+1
        print(multiplied_value)


multiplier(15)