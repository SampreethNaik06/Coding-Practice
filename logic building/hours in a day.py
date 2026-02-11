## to check for time and greet according to time
from datetime import datetime 
def greet():
    current_time = datetime.now().hour
    if 5<= current_time< 12:
        print("good morning")
    elif 12<=current_time<=17:
        print("good afternoon")
    elif 17<current_time<=21:
        print("good evening")
    else:
        print("good night")
        
greet()