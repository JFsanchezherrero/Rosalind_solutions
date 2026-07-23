# input file provided as sys.argv[1] element
import sys
with open(sys.argv[1]) as f:
  string2check = f.readline().strip()
  num_string = f.readline().strip()

print(string2check)
print(num_string)

## split string, convert to int and map to a list
list2get = list(map(int, num_string.split(" ")))

print(
    " ".join(
        [string2check[list2get[0]:list2get[1]+1],  ## substring 1
        string2check[list2get[2]:list2get[3]+1]])  ## substring 2
)
