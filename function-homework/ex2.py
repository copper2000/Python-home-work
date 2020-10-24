i = int(input("Input i: "))

def factorialCal(i):

    if(i == 0):
        return 1

    # recursive
    return i * factorialCal(i - 1)

print('Result: ' + str(factorialCal(i)))
