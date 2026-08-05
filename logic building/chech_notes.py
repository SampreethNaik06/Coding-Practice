# to check if an amount can be devided into 2000, 500 and 100 notes of amount 100
def check_notes(amt):
    if amt % 100 ==0:
        print( f'{amt} can be devided into notes of 100')
    else :
        print("not possible ")


    
    # for 2000,500,100 notes

    notes_2000 = amt//2000
    amt = amt%2000
    notes_500 = amt//500
    amt = amt%500
    notes_100 = amt//100
    amt = amt%100

    print(f'{notes_2000} in 2000 ')
    print(f'{notes_500} in 500 ')
    print(f'{notes_100} in 100 ')

check_notes(3500)