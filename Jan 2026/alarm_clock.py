# alarm clock app
# What are the things we need for this alarm clock?
# 1.) Seconds counter
# 2.) Get the current time
# 3.) Create a function which checks if something is at the same time
# 4.) Make a GUI that takes in the input of the time you want the alarm to go off

import time, sched
from time import gmtime, strftime


# get time function
def getTime():
    seconds = strftime("%a, %d, %b %Y %H: %M: %S", gmtime())
    return seconds

currentTime = getTime()
print(currentTime)

# create loop that runs each second

def detectTime(userInput):
    print("testing it now")
    x = 0
    y = userInput

    while y > 0:
        time.sleep(1.0)
        x += 1
        y -= 1
        print(x)
    print("Ending time now")

timerSet = 10
detectTime(timerSet)

# def do_something(scheduler): 
#     # schedule the next call first
#     scheduler.enter(60, 1, do_something, (scheduler,))
#     print("Doing stuff...")
#     # then do your stuff

# my_scheduler = sched.scheduler(time.time, time.sleep)
# my_scheduler.enter(60, 1, do_something, (my_scheduler,))
# my_scheduler.run()
