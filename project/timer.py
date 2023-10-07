import time

while True:
    choice = input("do you want to start? (y/n): ")
    if 'y' in choice.lower():
        hour = int(input("enter amount of hour: "))
        minutes = int(input("enter amount of minutes: "))
        seconds = int(input("enter amount of seconds: "))
        total = hour * 3600 + minutes * 60 + seconds
        print("timer starts now...")
        time.sleep(1)
        while total > 0:
            print(total)
            total -= 1
            time.sleep(1)
        print("timer end...")
    elif 'n' in choice.lower():
        print('exiting...')
        break
    else:
        print('invalid input...')
