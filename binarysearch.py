def binarySearch(low, high, arr, x):

    # Divide the array
    mid = (high + low) // 2

    while(low <= high):

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is greater than mid, then it can only
        # be present in right subarray
        elif mid < x:
            low = mid + 1
            return binarySearch(low, high, arr, x)  # call recursive

        # Else the element can only be present in left subarray
        else:
            high = mid - 1
            return binarySearch(low, high, arr, x)

    # If it not found any result
    return -1

def main():

    arr = []
    n = int(input("Enter number of elements: "))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)

    x = int(input("Search number: "))
    arrSize = len(arr)
    low = 0
    high = arrSize - 1

    result = binarySearch(low, high, arr, x)

    if result != -1:
        print("Element is present at index", str(result))
        print("Result =", arr[result])
    else:
        print("Element is not present in array")

main()
