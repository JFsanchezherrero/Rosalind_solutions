import sys

## input
mass_file2read = sys.argv[1]
seq_file = sys.argv[2]

## read as dictionary the table
d={}
with open(mass_file2read) as f:
    for line in f:
        line = line.strip()
        print(line)
        (key, val) = line.split()
        print("key: " + key)
        print("val: " + val)
        d[key] = float(val)

## read proteic sequence
with open(seq_file) as f:
  prot_string = f.read().strip()

## get value for each aa and sum all
print(sum([d[i] for i in prot_string]))