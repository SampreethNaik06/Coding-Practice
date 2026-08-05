# countdown timer with abort condition 

def abort(strt_num, abort_num):
    current_num = strt_num

    while current_num > 0:
        if current_num == abort_num:
            print("aborting")
            break  
        
        print(current_num)    
        current_num -= 1  
    
    if current_num == 0:
        print('blast off')

abort(7, 3)


