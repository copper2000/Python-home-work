# Bài 04: Viết hàm lấy giá trị 3 số bất kỳ trong khoảng 1~10. Kiểm tra xem đó có phải là 3 cạnh của 1 tam giác hay không

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
