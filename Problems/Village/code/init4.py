# input file provided as sys.argv[1] element
import sys
with open(sys.argv[1]) as f:
  num_string = f.readline().strip()

list2get = list(map(int, num_string.split(" ")))
total_sum = sum(filter(lambda x: x % 2, range(list2get[0], list2get[1] + 1)))
print(total_sum)