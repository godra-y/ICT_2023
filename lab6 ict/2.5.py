m = int(input("enter the first number : ")) 
n = int(input("enter the second number : ")) 
 
if (m < n) : 
    for i in range(m, n + 1) : 
        print(i) 
elif (m > n) : 
    for i in range(m, n - 1, -1) : 
        print(i) 
else :  
    print(m)
