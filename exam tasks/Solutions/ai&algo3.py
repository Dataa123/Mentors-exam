def convert(dec):
    res = ""
    while int(dec) != 0:
        res += str(int(dec) % 2)
        dec = str(int(dec) // 2)
    return res[::-1]

print(convert(32))
print(convert(31))
print(convert(8))
print(convert(29))
print(convert(98))
print(convert(251))
print(convert(16))
print(convert(138))