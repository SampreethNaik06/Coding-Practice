# given a tim with hours and minutes to check if the time given is am or pm

from datetime import datetime

def check_meridian(time):
    time_obj = datetime.strptime(time,"%H:%M")
    print(time_obj.strftime("%p"))
    
check_meridian("10:30")