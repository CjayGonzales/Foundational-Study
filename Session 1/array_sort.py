my_array = [0,1,3,7,6,5,9,8,10]

def array_sort(items):
    new_array = []
    previous_value = 0

    for item in items:
        if item > previous_value:
            previous_value = item
            new_array.append(item)
    
    print(new_array)
        

array_sort(my_array)
