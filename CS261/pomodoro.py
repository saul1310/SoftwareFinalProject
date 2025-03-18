import time

def minutes_to_seconds(study, rest): 
    """
    Converts the study and rest time from minutes to seconds.
    """
    study_num = int(study)
    rest_num = int(rest)

    study_sec = study_num * 60
    rest_sec = rest_num * 60
    return study_sec, rest_sec

def countdown_timer(seconds):
    """
    A countdown timer that prints the remaining time every second.
    """
    while seconds > 0:
        print(f'Time remaining: {seconds} seconds', end='\r')  
        time.sleep(1) 
        seconds -= 1
    print("The timer has ended, next session starting") 