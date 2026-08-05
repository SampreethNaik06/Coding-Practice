## balance every month 

def balance_op(balance):
    month = 0

    while balance<200:
        balance+=15
        month+=1

    print(f'for {month} the balance is {balance}')

balance_op(100)