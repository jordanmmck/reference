import math
import random
import fractions


f1 = fractions.Fraction(2, 3)
f2 = fractions.Fraction(1, 3)

sqrt2 = math.sqrt(2)
print(oct(12), hex(12), bin(12))
print(bin(5 | 4), bin(5 & 4), bin(5 ^ 4), bin(5 << 4), bin(5 >> 4), bin(~5))
n = 2**8
bit_len = n.bit_length()
n_bytes = n.to_bytes(4, 'big')

f = 0.83
print(f.as_integer_ratio())
print(f.is_integer())

# random
rand_num = random.randrange(0, 10)
