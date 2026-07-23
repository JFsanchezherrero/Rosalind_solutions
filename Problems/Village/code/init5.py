# input file provided as sys.argv[1] element
import sys
with open(sys.argv[1]) as f:    
  all_doc_list = f.readlines()

dict_text={}
for i in range(len(all_doc_list)):
    dict_text[i]=all_doc_list[i]

list_even_items = list(filter(lambda x: x % 2, dict_text.keys()))
phrases_ = [dict_text[item] for item in list_even_items]

print(str("".join(phrases_)))