from collections import defaultdict
from Bio import SeqIO
import sys

sequences_record =[]
with open(sys.argv[1]) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        ## save sequence & length
        sequences_record.append(record)


### create the adjacency list
adjacency_list = defaultdict(int)
adjacency_list2 = defaultdict(list)

k=3
for i in sequences_record:
    for j in sequences_record:

        ## prevent directed loops
        if (i.id != j.id):
            #print("i: " + i.id + " ---- " + "j: " + j.id)

            ## check suffixes match prefixes of length k: Directed graph
            if (i.seq[-k:] == j.seq[0:k]):

                list_edges = [i.id, j.id]
                #slist_edges = sorted(list_edges)
                
                adjacency_list2[list_edges[0]].append(list_edges[1])
                list_edges_str = "---".join(list_edges)

                adjacency_list[list_edges_str] +=1





## print output
print("\n".join([str(k.split("---")[0]) + " " + str(k.split("---")[1]) for k in adjacency_list.keys()]))