#importing time and threading modules
import time
import threading
#making the CountdownTimer class that contains all required timerfunctions
class CountdownTimer:
    def __init__(self, minutes):
        self.minutes = minutes
        self.seconds = minutes * 60
        self.is_running = False
    #defining the start function that starts our timer
    def start(self):
        self.is_running = True
        while self.is_running and self.seconds:
            self.seconds -= 1
            minutes, seconds = divmod(self.seconds, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(f"Time Left: {timer}", end="\r")
            #using time.sleep() function to delay the timer output to one second
            time.sleep(1)
            #print the time's up message if the timer runs out
            if(seconds==0):
                print("Time's up!")
    #defining the reset function
    def reset(self):
        self.is_running = False
        self.seconds = self.minutes * 60
    #defining the stop function
    def stop(self):
        self.is_running = False
    #defining the pause function
    def pause(self):
        self.is_running = False
    #defining the resume function
    def resume(self):
        self.is_running = True
        self.start()
# Create a timer object with user defined input minutes
n=int(input("Enter the value in minutes of the timer: "))
#calling the CountdownTimer class as timer
timer = CountdownTimer(n)
#defining the thread function so that the timer goes on while we may enter some input command
t1=threading.Thread(target=timer.start)
t2=threading.Thread(target=timer.stop)
t3=threading.Thread(target=timer.reset)
t4=threading.Thread(target=timer.resume)
t5=threading.Thread(target=timer.pause)
# Allows user to enter commands
#threading the functions once again so that they can be started multipletimes
while(True):
    command = input("Enter a command (reset, stop, pause, start, resume,or exit):\n")
    if command == "reset":
        t3.start()
        t3=threading.Thread(target=timer.reset)
    elif command == "stop":
        t2.start()
        t2=threading.Thread(target=timer.stop)
    elif command == "pause":
        t5.start()
        t5=threading.Thread(target=timer.pause)
    elif command == "resume":
        t4.start()
        t4=threading.Thread(target=timer.resume)
    elif command == "start":
        t1.start()
        t1=threading.Thread(target=timer.start)
    elif command == "exit":
        break
    else:
        print("Invalid command")