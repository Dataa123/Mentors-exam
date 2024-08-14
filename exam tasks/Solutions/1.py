def check_walk(listn):
    if len(listn) != 10:
        return False
    
    op = {
        "w": "e",
        "n": "s",
        "s": "n",
        "e": "w"
    }
    is_true = True

    for i in listn:
        if listn.count(i) == listn.count(op[i]):
            is_true = True
        else:
            is_true = False
            break
    
    return is_true
    

print(check_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # False
print(check_walk(['n','s','n','s','n','s','n','s','n','s'])) # True
print(check_walk(['n','n','n','s','n','s','n','s','n','s'])) # False
print(check_walk(['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'])) # False
print(check_walk(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'])) # True