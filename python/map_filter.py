# map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

# filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
