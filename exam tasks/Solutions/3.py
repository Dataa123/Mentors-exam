def expand(num):
    num = str(num)
    l = len(num)
    res = []

    for i in num:
        if i != "0":
            res.append(f"{i}{(l - 1) * "0"}")
        l -= 1

    return " + ".join(res)

print(expand(70304)) # '70000 + 300 + 4'
print(expand(42)) # '40 + 2'
print(expand(710163)) # '700000 + 10000 + 100 + 60 + 3'
print(expand(853546)) # '800000 + 50000 + 3000 + 500 + 40 + 6'
print(expand(511604)) # '500000 + 10000 + 1000 + 600 + 4'