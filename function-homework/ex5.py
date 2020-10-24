# Fibonacci formula: F{n} = F{n-1} + F{n-2}

# define an array to store value
fibo = []

def fibonacci(n):
    
    if(n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        # recursive
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(0, 20):    
    fibo.append(fibonacci(i))

print('The first 20 numbers in the Fibonacci sequence: ' + str(set(fibo)))
    

