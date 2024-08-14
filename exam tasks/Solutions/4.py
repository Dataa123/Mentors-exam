def identifier(listn):
    even_count = 0
    odd_count = 0

    for i in range(len(listn)):
        if i == 3:
            break
        if listn[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return "even" if even_count > odd_count else "odd"

def outlie(listn):
    identify = identifier(listn)
    if identify == "even":
        return list(filter(lambda x: x % 2 != 0, listn))[0]
    else:
        return list(filter(lambda x: x % 2 == 0, listn))[0]

print(outlie([2, 4, 0, 100, 4, 11, 2602, 36])) #  11
print(outlie([160, 3, 1719, 19, 11, 13, -21])) # 160
print(outlie([7516484, 526386, 1637037, 813302, -8496994, 812820, 3797630, -3773758, 921354, 6123650, 1693668])) # 1637037
print(outlie([8811272, 9218790, 9094178, -818772, 2711934, -3905606, 1332109])) # 1332109
print(outlie([-4207752, 362590, 5205484, 11340, 3740336, 1360605])) # 1360605