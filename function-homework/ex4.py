import random

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

# define some constants
INVALID_MESSAGE = 'Invalid triangle'
VALID_MESSAGE = 'Valid triangle'

def checkTriangleEdge(a, b, c):
 
    if((a + b < c) or (a + c < b) or (b + c < a)): 
        return INVALID_MESSAGE
    else: 
        return VALID_MESSAGE

print(str(checkTriangleEdge(a, b, c)))
