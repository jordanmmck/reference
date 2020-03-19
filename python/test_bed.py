def f(a, b):
    print(a, b)


d = {'x': 123, 'y': 456}
f(d, d.pop('x'))
