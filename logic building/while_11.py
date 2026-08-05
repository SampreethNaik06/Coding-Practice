# atm cash withdraw machine

def atm_withdraw(account_balance, withdrawal_amount):

    while account_balance >= withdrawal_amount:
        account_balance = account_balance-withdrawal_amount
        print(f"withdraw {withdrawal_amount}, remaining {account_balance}")

    print( f"Insufficient funds for another withdrawal! Final balance: {account_balance}")   

atm_withdraw(100,30)