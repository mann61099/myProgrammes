def showPrimes(n):
    prime=[True for i in range(n+1)]    #Creating a boolean array of true values
    p=2
    while (p*p<=n):
        if (prime[p]==True):
            for i in range(p*p,n+1,p):  #Cancelling out multiples of prime numbers
                prime[i]=False            
        p+=1                            #This way eventually all composite values become false  
        
    for p in range(2,n):                #The indexes of array having true values are prime numbers
        if prime[p]:
            print(p),


a=int(input("Enter number: "))
if (a>1):
    print ("Showing all the prime numbers smaller than or equal to ",a)
    showPrimes(a)
else: print("Invalid Input!")

