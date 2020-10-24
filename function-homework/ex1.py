# define an array to store i value
arr = []

# define some constants
START = 2000
END = 3200
WHITE_SPACE = ' '
COMMA = ','

def multipleDivisor(START, END):

    for i in range(START, (END + 1)):

        if (i % 7 == 0 and i % 5 != 0):
            # add i to array
            arr.append(str(i))

    return (COMMA + WHITE_SPACE).join(arr)

print(str(multipleDivisor(START, END)))
