l1 = ['x', 'y', 'z']
l2 = [2, 3, 5, 7]
l3 = [0] * 3

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
