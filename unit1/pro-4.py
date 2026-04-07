for i in range(10):
    num = int(input("Enter number: "))
    temp = num
    s = 0
    digits = len(str(num))
    
    while temp > 0:
        d = temp % 10
        s += d ** digits
        temp //= 10
    
    if num == s:
        print(num)
