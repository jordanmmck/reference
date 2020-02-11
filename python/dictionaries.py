d1 = dict(a=1, b=2, c=3)
print(d1)

d = {'a': 1, 'b': 2, 'c': 3}
print(sorted(d))  # or make it a list then sort it then print it
print(d)
del d['a']
d['b'] = 777
print(d.get('z'))
print(d.get('b'))
print(d.keys())
print(d.values())
print(hash('jordan'))
dvar = d['z'] if 'z' in d else 0

# # {0:0, 1:0, 2:0, ...}, if the ,0 is omitted then Nones
D = dict.fromkeys((range(5)), 0)
if 1 in d:
    d[1] += 1
else:
    d[1] = 1

print(D)
