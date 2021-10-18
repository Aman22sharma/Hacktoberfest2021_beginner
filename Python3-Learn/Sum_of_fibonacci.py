def calculateSumFibo(n) :
    if (n <= 0) :
        return 0
  
    fibo =[0] * (n+1)
    fibo[1] = 1
  
    # Initialize result
    sm = fibo[0] + fibo[1]
  
    # Add remaining terms
    for i in range(2,n+1) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        sm = sm + fibo[i]
         
    return sm
 
 
n = int(input("Enter the Value of n: "))
print("Sum of Fibonacci numbers is : " ,
      calculateSumFibo(n))
