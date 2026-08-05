# savings goal 


def reach_savings_goal(target_amount, deposit):

    total_savings = 0
    count = 0 

    while total_savings < target_amount:
        total_savings +=  deposit
        count+=1 

    print(f"target reached  in {count} weeks ")


reach_savings_goal(120,20)