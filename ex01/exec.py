import sys

s = (' ').join(sys.argv[1:])
s_swap = s.swapcase()
l = list(s_swap)
l.reverse()
print(''.join(l))