x = 0
print("1.", x)


def fn1():

    x = 1
    print("2.", x)

fn1()

print("3.", x)


def fn2():
    global x
    x = 1
    print("4.", x)
    return x

fn2()

print("5.", x)
