l1 = ['x', 'y', 'z']
l2 = [2, 3, 5, 7]
l3 = [0] * 3

print('x' in l1)
l1.index('y')

truthy = [1, ['a'], True, 'true']
print(all(truthy))

falsey = [0, [], False, '']
print(any(falsey))

# insert at index 0
l3.insert(0, 1)
# remove the number 1
l3.remove(1)

mini = min(l2)
maxi = max(l2)

# combine lists into iterator of tuples
l1_l2_pairs = zip(l1, l2)

# get l1 reversed
l1_reversed = l1[::-1]

a = [1, 2, 3, 4, 5]

a[:]
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

'''
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]
a[start:stop:step] # start through not past stop, by step
'''

# comprehensions
l4 = [[i, j] for i in range(5) for j in range(6) if i + j != 10]
l4 = [[x**2, x**3] for x in range(5)]
l4 = [i for i in range(5) if i % 2 == 0]
