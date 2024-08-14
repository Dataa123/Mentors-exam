def check_decimal(arr):
    if arr == []:
        return True
    
    for i in arr:
        if type(i) is str:
            return False

    arr = [str(i) for i in arr]
    is_true = True

    for i in arr:
        if i.isdigit():
            is_true = True
        else:
            if i[-2:] == ".0":
                is_true = True
            else:
                is_true = False
                break

    return is_true


print(check_decimal([])) # True
print(check_decimal([1, 2, 3, 4])) # True
print(check_decimal([1.0, 2.0, 3.0])) # True
print(check_decimal([1.0, 2.0, 3.0001])) # False
print(check_decimal(["-1"])) # False

