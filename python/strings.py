print('\n' * 2)

# format
print("{i}: {item}".format(i=4, item='test'))
print('{}, and {}'.format('thing1', 'thing2'))

# 314,151.99
print('{:,.2f}'.format(314151.99234))
print("No newline ", end="")

# multiline
s = """
1
2
3
"""
print(s)

s = "pip is for pip installs python"
s.capitalize()

print("The word 'pip' appears " + str(s.count("pip")) + " times")
t = "----title----"
print(t.center(30))

s = "pip is for pip installs python"
print(s.find("pip"))
print(len(s))
r = "file.txt"
print(r.endswith(".txt"))

word_list = s.split(" ")
print(word_list)
joined_words = "-".join(word_list)

# slice notation
print(s[2:])

# get ascii value
print(ord('c'))
eval("2+2")
