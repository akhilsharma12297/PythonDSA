def starter():
    arr = [10, 3, 5, 6, 20]

    print(func(arr, 0, 1, -1, 1))


def func(arr, idx, ctr, maxValue, currProduct):

    if(ctr == 3):
        return maxValue
    
    if idx >= len(arr):
        if maxValue > currProduct:
            maxValue = currProduct
        return maxValue
    
    return max(func(arr, idx + 1, ctr + 1, max, currProduct * arr[idx]), func(arr, idx + 1, ctr, max, currProduct))


starter()
