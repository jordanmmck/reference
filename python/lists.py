# make list of the same immutable item
# these are references to the same item!
four_nones = [None] * 4
L = ['a', 'b', 'c', 'd']
L[0] = 'z'
# print(L[1:3])
# print(L[-1]) # this is actually L[len(L)-1]
# print(L[1:])
L.append('x')
L.insert(0, 'A')
print(L)
L.remove('c')
L.pop()

del L[1]
L = sorted(L + ['zzz'])
L.reverse()
print(L)
L = [1, 2, 3]
z = len(L) + min(L) + max(L)
S = ['a', 'b', 'c']
s = ''.join(S)
L.clear()
print(L)

L = [[i, j] for i in range(6) for j in range(6) if i + j != 10]
# print(L)
T = [[x**2, x**3] for x in range(4)]
# print(T)
m = [[1, 2, 3], [4, 5, 6]]
col1 = [row[1] for row in m]
# print(col1)
V = [i for i in range(10) if i % 2 == 0]
print(V)
