# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes
 
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1):
        if prime[p]:
            print(p)
 
# Run the program
if __name__=='__main__':
    n = 30 # range 0-30 
    print("Following are the prime numbers smaller than or equal to " + str(n)) 
    SieveOfEratosthenes(n)