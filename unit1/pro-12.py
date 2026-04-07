x = 10  # global variable

def outer():
    y = 5  # local variable in outer()

    def inner():
        nonlocal y  # refers to y in outer()
        y += 10
        print("Inner nonlocal y =", y)

    inner()
    print("Outer local y =", y)

outer()
print("Global x =", x)
