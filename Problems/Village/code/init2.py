
# input file provided as sys.argv[1] element
import sys
with open(sys.argv[1]) as f:
  num_list = f.read().strip().split(" ")

a=int(num_list[0])
b=int(num_list[1])

## calculate
h2 = a*a + b*b
print(h2)