
i = "Hello world, Im re-learning how to code because I have fallen off it. Please let me get better at coding again"
dict_var = {
    "test": "test",
    "test again": 2
}

my_set = {"item 1", "item 2", "item 3"}

#unchangable array
my_frozen_set = frozenset(my_set)

my_broken_set = my_set.add("Test")

def data_sort(x):

    # error handling
    if x is None:
        print("Please enter something")

    val = type(x)
    
    if val == int:
        print("I am a int: " + str(x))
    elif val == str:
        print("I am a string: " +x)
    elif val == float:
        print("I am a float: " + str(x))
    elif val == complex:
        print("I am a complex: " + str(x))
    elif val == dict:
        print("I am a dictionary: " + str(x))
    elif val == set:
        print("I am a set: " + str(x))
    elif val == frozenset:
        print("I am a frozenset: " + str(x))
    
# data_sort(complex(3, 2))
data_sort(i)





