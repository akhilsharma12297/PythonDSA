def starter():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    val = 7
    fun(val, arr)


def fun(val, arr):
    Flag = func_helper(0, val, arr)

    if Flag:
        print("Found at", idx)
    else:
        print("Not Found !!")


def func_helper(idx, val, arr):
    if idx == len(arr):
        return False
    
    func_helper(idx + 1, val, arr)

    if val == arr[idx]:
        return True


starter()
