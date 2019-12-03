a = [5, 10, 15, 20, 25, 30]

def func():
    b = []
    b.extend([a[0], a[-1]])
    print(b)


func()