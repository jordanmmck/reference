L = {0, 1, 2, 2, 3, 5}
M = set([2, 3, 5])
N = set('abcdeef')
print(N)
# intersection
print(L & M)
# union
print(L | M)
# diff
print(L - M)
# symmetric diff
print(L ^ M)
# L superset of M?
print(L > M)
L.add(9)
L.pop()
L.remove(2)
L.discard(1)
# set comprehension
P = {n**2 for n in range(10)}
print(set('abcde') == set('edcba'))
