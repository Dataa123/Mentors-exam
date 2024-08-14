def prime(num):
    count = 0
    for i in range(1, int(num ** 0.5)):
        if num % i == 0:
            count += 1

    return count <= 2

def gap(g, m, n):
    for i in range(m, n):
        if prime(i) and prime(i + g):
            return [i, i + g]
    return None
        
print(gap(6, 585348, 685348)) # [585437, 585443]
print(gap(8, 585348, 685348)) # [585383, 585391]
print(gap(2, 517184, 526184)) # [517241, 517243]
print(gap(6, 100, 110)) # None
print(gap(2, 100, 103)) # [101, 103]