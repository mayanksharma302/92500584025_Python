def total(*args):
    sum = 0
    for num in args:
        sum += num
    print("Total =", sum)

total(10, 20, 30, 5)
