
#example 1
def look_for_key(box):
 for item in box:
    if item.is_a_box():
        look_for_key(item) # Recursion!
    elif item.is_a_key():
        print("found the key!")

#example 2
def till_zero(item):
   print(item)
   if item <= 0:
      return
   else:
    till_zero(item -1)

# till_zero(20)

# call stack factorial

def find_fact(x):
    if x == 1:
      return 1
    else:
      mult = x * find_fact(x-1)
      print(mult)

      return x * find_fact(x-1)
    
# find_fact(3)
      


def key_finder(box):
   x=0
   if box == "key":
      print("Found key!")
      return 
   else:
      key_finder(box[-1])
      print(x)
      x += 1

key_finder(["box","box","box","box","box","box","key"])
