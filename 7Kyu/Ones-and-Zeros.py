def binary_array_to_number(arr):
    number=0
    inv_arr = arr[::-1]
    print(inv_arr)
    for i in inv_arr:
        if i == 1:
            print(2**inv_arr.index(i))
            number+=(2**inv_arr.index(i))
            inv_arr[inv_arr.index(i)]=0
    return number