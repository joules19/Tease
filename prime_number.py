def isPrime(n):
    if n < 2:
        print("Invalid Input")
        return

    i = 2
    while i <= (n / 2):
        if n % i == 0:
            print("not prime number")
            return
        i +=1
  
    print("is prime number")
        
isPrime(21)
