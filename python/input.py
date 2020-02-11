import sys

print('2 space sep ints')
a, b = map(int, input().strip().split(' '))

print('many space sep ints')
C = list(map(int, input().strip().split(' ')))

print('a string')
name = sys.stdin.readline()

print('an int')
x = int(input("Enter a num: "))

print('anything')
myString = input()
