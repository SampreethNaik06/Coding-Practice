# to check if an amount can be devided into 2000, 500 and 100 notes of amount 100
def check_notes(amount):
    if amount%100 != 0:
        print("the amount cannot be devided into 100 notes")
        return
    elif amount% 100 == 0:
        print("amount can be devided into 2000,500 and 100 notes")
    
    ## to check how many notes
    notes_2000 = amount//2000
    amount = amount%2000
    notes_500 = amount//500
    amount = amount%500    
    notes_100 = amount//100
    print(f"number of 2000 notes: {notes_2000}")
    print(f"number of 500 notes: {notes_500}")
    print(f"number of 100 notes: {notes_100}")
    
check_notes(3700)
check_notes(3850)   