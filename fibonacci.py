def fib(n):
    f1 = f3 = 0
    f2 = 1
    
    arr = []
    output = ""
    for i in range(n):
        if len(arr) < 1:
            arr.append(f1)
            arr.append(f2)
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        arr.append(f3)

    print(" ".join(map(str, arr)))