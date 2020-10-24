import math

a = int(input("Input edge a: "))
b = int(input("Input edge b: "))
c = int(input("Input edge c: "))

# define some constants
ERROR_VALIDATE = 'The value must not be less than or equal to 0'
ERROR_CHECK = 'Invalid triangle'

# validate value
if(a <= 0 or b <= 0 or c <= 0):
    print(ERROR_VALIDATE)
    exit()

# check triangle inequality
if((a + b < c) or (a + c < b) or (b + c < a)):
    print(ERROR_CHECK)
    exit()
    
def triangleArea(a, b, c):
    # calculate perimenter
    p = a + b + c 

    # apply the heron formula
    heron = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return heron

print('Result: ' + str(round(triangleArea(a, b, c))))
     
