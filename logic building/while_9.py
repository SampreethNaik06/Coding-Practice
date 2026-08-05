# battery drain while function problem 

def batterydrain(battery):

    while battery>=20:
        print(f"battery at: {battery}")
        battery = battery - 15

    print("low battery")

batterydrain(50)