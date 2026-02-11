#print days from numbers

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

num = int(input("Enter a number (1-7): "))

print(days.get(num, "Invalid input. Please enter a number between 1 and 7."))
