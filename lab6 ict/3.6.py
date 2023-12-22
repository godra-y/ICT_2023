m = int(input("enter the first number : ")) 
n = int(input("enter the second number : ")) 
 
if (m > n) : 
    for i in range(m, n - 1, -1) : 
        if (i % 2 != 0) : 
            print(i) 
else : 
    print("invalid condition, m must be greater than n") 
 
 
for i in range(m, n - 1, -1): 
    if i % 2 != 0: 
        print(i)
