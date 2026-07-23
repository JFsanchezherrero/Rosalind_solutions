# input file provided as sys.argv[1] element
import sys

## read dna_string information as two separate string
with open(sys.argv[1]) as f:
  s1 = f.readline().strip()
  s2 = f.readline().strip()

if (len(s1) != len(s2)):
  print("Different length between sequences...")
  exit()

hm = sum(a != b for a, b in zip(s1, s2))
print(hm)