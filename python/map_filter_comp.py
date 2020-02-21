# lists
l4 = [[i, j] for i in range(5) for j in range(6) if i + j != 10]
l4 = [[x**2, x**3] for x in range(5)]
l4 = [i for i in range(5) if i % 2 == 0]

# dicts
d = {n: n**2 for n in range(5)}

# set comprehension
P = {n**2 for n in range(10)}

# map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

# filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
