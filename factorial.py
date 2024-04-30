def factorial(val):
    output = 1
    for i in range(val + 1):
        if i == 0:
            pass
        else:
            output = output * i

    print(output)

#factorial(5)

def factorial1(val):
    if val < 0:
        return 0
    elif val == 0 or val == 1:
        return 1
    
    output = 1
    while val > 1:
        output *= val


    output = 1
    for i in range(val + 1):
        if i == 0:
            pass
        else:
            output = output * i

    print(output)

factorial1(-1)