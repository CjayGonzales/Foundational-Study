# create a function that swaps different variables to another variable.

# 1: Define the function with parameter of the variable
# 2: Store the variable
# 3: Return the new variable


def store_variable(x, y):
    x = x
    y = y
    store = x
    x = y
    y = store

    print(x, y)

store_variable("Hello World", "Swapped places")
