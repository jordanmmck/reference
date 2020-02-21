# Regex

## Character Classes

. any char except newline
\w word
\W not word
\d digit
\s whitespace
[abc] any of a,b,c
[^abc] not a,b,c
[a-d] chars between a-d

## Anchors

^abc\$ start to end

## Quantifiers

a\*, a+, a? 0 or more, 1 or more, 0 or 1
[0-9]{4} match groups of 4 nums
a{2,} match 2 or more a's
ab|cd match ab or cd

## Other

. anything but \n
a{20} 20 copies of a
a{3,5} 3-5 copies of a (greedy)
a{3,5}? 3-5 copies of a (nongreedy)
[] a set of chars
[^5] all chars except 5
a|b a or b

## Look Around

(?<=X) positive look behind assertion
(?<!X) negative look behind assertion
(?=X) positive look ahead assertion
(?!X) positive look ahead assertion
