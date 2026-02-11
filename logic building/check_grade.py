#to check for the marks and return the corresponding grade
def check_marks(grade):
    if grade<0 or grade>100:
        print("invalid grade")
    elif grade>=90:
        print("grade A")
    elif grade>=80:
        print("grade B")
    elif grade>=70:
        print("grade C")
    elif grade>=60:
        print("grade D")
    else:
        print("grade F")    
        
        
        
check_marks(95)
check_marks(85)