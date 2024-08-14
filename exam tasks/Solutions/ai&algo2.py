def check_capitals(string):
    count = 0

    for i in string:
        if i.isupper():
            count += 1

    return count

print(check_capitals("Hello WOrld"))
print(check_capitals("Hello WOrlD"))
print(check_capitals("HELLOWORLD"))

# How many comparisons does it do? answer: N
# What is the fewest number of increments it might do? answer: 0
# What is the largest number? N