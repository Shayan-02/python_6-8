from time import sleep
def countdown_timer(seconds: int):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        sleep(1)
        seconds -= 1
    print("Time's up!")
hour = int(input("enter amount of hour: "))
minutes = int(input("enter amount of minutes: "))
seconds = int(input("enter amount of seconds: "))
total = hour * 3600 + minutes * 60 + seconds
countdown_timer(total)
