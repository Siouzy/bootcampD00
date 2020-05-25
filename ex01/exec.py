import sys

s = (' ').join(sys.argv[1:])
s_swap = s.swapcase()
li = list(s_swap)
li.reverse()
print(''.join(li))
