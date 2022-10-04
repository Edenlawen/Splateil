import time
 
secondes = 5
 
 
def Timer(seconds=16):
    print("Début chrono : 40s")
    for i in range(seconds):
        print(seconds)
        time.sleep(1)
        seconds -= 1
    if seconds == 0:
        print("Fin")

Timer()