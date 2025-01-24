from pygame import mixer
from datetime import datetime
import time

def alarm_clock(alarm_time):
    print(f"Alarm Set for {alarm_time}")
    music_file = "output.mp3"
    alarm = True
    
    while alarm:
        current_time=datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Time to wakey wakey 😫😫")
            mixer.init()
            mixer.music.load(music_file)
            mixer.music.play()
            while mixer.music.get_busy():
                pass

            alarm = False
    
        time.sleep(1)

alarm_time = input("Enter the time(%H:%M:%S): ")

alarm_clock(alarm_time)