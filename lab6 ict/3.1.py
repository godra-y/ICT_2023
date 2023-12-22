number = int(input("enter the number : ")) 
 
if (1 <= number <= 20) : 
    for i in range(number) :  
        print('*' * 19) 
else : 
    print("enter a valid natural number between 1 to 20 ! ")