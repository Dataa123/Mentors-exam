def pig_latin(string):
    res = []
    string = string.split()

    for i in string:
        res.append(i[1:] + i[0] + "ay")

    return " ".join(res)

print(pig_latin('Pig latin is cool')) # 'igPay atinlay siay oolcay'
print(pig_latin('This is my string')) # 'hisTay siay ymay tringsay'
print(pig_latin("Ultima necat")) # 'ltimaUay ecatnay'
print(pig_latin("Lux in tenebris lucet")) # 'uxLay niay enebristay ucetlay'
print(pig_latin("Cucullus non facit monachum")) # 'ucullusCay onnay acitfay onachummay'