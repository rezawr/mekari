# Fibonacci

def fibonacci(limit):
    tmp = 0
    fibo = []
    result = 0

    for x in range(limit):
        if x == 0:
            result = 0
        elif x == 1:
            result = 1
        else:
            result = tmp + result
            tmp = fibo[x-1]

        fibo.append(result)

    return fibo


print(fibonacci(3))
