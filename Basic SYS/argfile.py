import sys

name = sys.argv[1]
handle = open(name, 'r')
text = handle.read()
print(name, 'is', len(text), 'bytes')

#more
import sys

print('Count:', len(sys.argv))
print('Type:', type(sys.argv))

for arg in sys.argv:
    print('Argument:', arg)
