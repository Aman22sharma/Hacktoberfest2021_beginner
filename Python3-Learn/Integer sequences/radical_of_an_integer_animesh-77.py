### AUTHOR: Animesh
##Python3 Concept: Find radical of a positive integer
## GITHUB: https://github.com/animesh-77

''' this program prints the radical of an inputted positive integer 
the definition of radical of an integer can be found here
https://en.wikipedia.org/wiki/Radical_of_an_integer
'''


def main():
    """
    main function of the program for inputs and functions calling.

    """
    
    error_message = "Invalid input, please enter a non-negative integer"

    try:
        # take user input
        n = input("Please enter a non-negative integer: ")

        final= radical_integer(int(n))
        print ("radical of ",n," is = ",final)
    
    except KeyboardInterrupt:
        print("----ABORTED!----") # If the program is stopped with ctrl+c
        return
    except TypeError:
        print(error_message) # In case the user inputs something different from numbers
        return
    except ValueError: # In case user inputs a different value than integer
        print(error_message)
        return
    except:
        logging.exception("ERROR: ") # Shows any kind of message with the full stack trace in case we don't know what exception ocurred

    if int(n) < 0:  # n cannot be less than zero
        print(error_message)
        return

    


def radical_integer(n):
    
    if (n==0):
        return 0 # 0 has no factors

    rad=1
    for i in range(1,n+1): # loop from 1 to inputted number
        if is_prime(i) and n%i==0: # if i is prime and a factor of n
            rad*= i 

    return rad

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization.
        https://en.wikipedia.org/wiki/Primality_test"""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


            
if __name__ == "__main__":
    main()



        
        
