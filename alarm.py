from datetime import datetime

from playsound import playsound
user_input = input('Set an alarm(time):')

try:
    current_hour = datetime.now().hour

    if 'a' in user_input.lower():
        hour = int(user_input[0])
    else:
        hour = int(user_input[0]) + 12

    while True:
        current_min = datetime.now().minute
        u_hour, u_min = user_input.split(':')
        minute, space = u_min.split(' ')
        if current_min == int(minute):
            while True:
                playsound('AlermMusic.mp3')

            break
        else:
            current_hour = datetime.now().hour

except BaseException:
    print("Hey,make sure you've entered a valid tme.The valid time format is 'hour:minute A.M/P.M")
    print("For example: 7:15 P.M")
