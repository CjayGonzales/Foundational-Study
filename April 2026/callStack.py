
def function1(name):
    print("Hello there", name)

def function2(param):

    if param :
        name = param
    else :
        name = "Default"
    
    function1(name)

    return

def function3(param):
    function2(param)

function3(param = None)



