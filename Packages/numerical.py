#Function to check if number isprime

def isPrime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if(count==2):
        return True
    else:
        return False
    
#Function to determine number of prime factors for a given number
def numberPrimeFactors(n):
    if isPrime(n):
        return 1
    count=0
    for i in range(2,n//2+1):
        if isPrime(i) and n%i==0:
            count+=1
    return count
