
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

till_zero(20)


      