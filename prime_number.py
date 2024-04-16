def isPrime(n):
    i = 2
    while i < (n / 2):
        print(i)
        if n % i == 0:
            print("not prime")
    print("is prime")
        
isPrime(31)
