def print_all_public_fields(obj):
    print(obj)
    for a in dir(obj):
        if not a.startswith('_') and not a.isupper():
            print('\t%s = %s' % (a, getattr(obj, a)))


t = (3, 5, 7, 11)

print('All the methods')
print(dir(t), end='\n\n')

# get info on the function!
# help(str.replace)

print('The type of this tuple')
print(type(t), end='\n\n')

print('The id of this tuple')
print(id(t), end='\n\n')

print('All public array methods')
print(print_all_public_fields([1, 2, 3]))
