
def recursive_function(recursion):
    print("Hello thhere recursion" + recursion)
    recursive_function(recursion=recursion)
    
    return

pass_through = "Passing in"
# recursive_function(pass_through)

def recursive_function_2(param1):

    print("reursive func print",param1)

    if (param1 > 10):
        print("Recursive func in if ", param1)
        recursive_function_2
        return
    else:
        print(param1)
        return


    return

recursive_function_2(20)