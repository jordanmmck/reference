import os

count = 0
for line in open('python.txt'):
    count += 1
print(count)

file1 = open("temp1.txt", "w+")
file1.write("test123\n")
text_infile = file1.read()
file1.close()
os.remove("temp1.txt")

# r     read from beginning
# r+    read/write from beginning
# w     start fresh for writing
# w+    start fresh for read/write
# a     open for writing, write to end
# a+    open for read/write, at end
