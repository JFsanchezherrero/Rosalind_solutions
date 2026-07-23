# input file provided as sys.argv[1] element
import sys
with open(sys.argv[1]) as f:    
  all_doc_list = f.readline().strip()

from collections import defaultdict
dict_text = defaultdict(int)

for word in all_doc_list.split():
    dict_text[word] += 1

print(dict_text)

for x in dict_text.keys():
    print(x, str(dict_text[x]), sep=" ")