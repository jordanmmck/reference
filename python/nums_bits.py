import fractions
import decimal
import random
import math

f1 = fractions.Fraction(2, 3)
f2 = fractions.Fraction(1, 3)
print(f1 + f2)
print(bool(2))
c = 1 + 2j
d = decimal.Decimal('3.14159999')
rand_num = random.randrange(0, 10)
print(rand_num)
print(math.sqrt(9))
print(oct(12))
print(hex(12))
print(bin(12))
print(bin(5 | 4))
print(bin(5 ^ 4))
print(bin(5 & 4))
print(bin(5 << 1))
print(bin(5 >> 1))
print(bin(~5))
n = 1999
print(n.bit_length())
print(n.to_bytes(4, 'big'))
f = 0.83
print(f.as_integer_ratio())
print(f.is_integer())
