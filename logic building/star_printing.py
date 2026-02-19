### this file contains all the code  where i have practiced star printing for for loop practice and logic building 


# to print a single star
print("*")

# to print four stars
for i in range(2):
    print("*",end  = "")
    
# to print * in nxn format 
for i in range(5):
    for j in range(4):
        print("*", end="")
    print()




# to print stars in triangle shape

for i in range(1,6):
    for j in range(i):
        print("*",end ="")
    print()
    
    
# Print a Right-Aligned Triangle of Stars

n = 5 
# to print spaces
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end  ="")
# for printing stars
    for k in range(i):
        print("*",end = "")
    print()
    
    
# Print Stars in Even Numbers (2, 4, 6, 8, 10)
for i in range(1,6):
    for j in range(i):
        print("*"*2,end = "")
    print()
    
# Print Stars in Odd Numbers (1, 3, 5, 7, 9)

for i in range(1,6):
        print("*" * (2*i - 1))
print()

# print a centered pyramid of stars

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end = "") # we print spaces
    for k in range(2*i-1):
        print("*",end  = "")
    print()
    
    
# question 10 

for i in range(n-1):
   for  j in range(n-1-i):
        print("b",end = "")
print()