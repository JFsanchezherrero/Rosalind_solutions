# input file provided as sys.argv[1] element
import sys

## read dna_string information as two separate string
with open(sys.argv[1]) as f:
  s_seq = f.readline().strip()
  t_seq = f.readline().strip()

print("s_seq: " + s_seq)
print("t_seq: " + t_seq)

## traverse and get hits
hits = []
while(s_seq.find(t_seq) > 0):
    hit_pos = s_seq.index(t_seq)
    s_seq = s_seq[hit_pos+1:]
    try:
        hits.append(hits[-1]+hit_pos+1)
    except:
        hits.append(hit_pos+1)

print(" ".join(map(str, hits)))
