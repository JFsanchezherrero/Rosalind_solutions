from Bio import SeqIO
from Bio.Seq import Seq
import sys


sequences_record =[]
with open(sys.argv[1]) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        ## save sequence & length
        sequences_record.append(record)

genomic_dna = str(sequences_record[0].seq)
start_bp=0
final_str=genomic_dna

for i in range(1, len(sequences_record)):
    intron_seq = str(sequences_record[i].seq)

    print("--------------------------------")
    print("Intron sequence: ")
    print(intron_seq)
    print("--------------------------------")
    if final_str.index(intron_seq):
        index_intron = final_str.index(intron_seq)
        end_bp = index_intron + len(intron_seq)

        print("Coordinates: ")
        print("First:  start - end: " + str(start_bp) + " - " + str(index_intron))
        print("Second: start - end: " + str(end_bp) + " - End" )
        
        final_str = final_str[start_bp:index_intron] + final_str[end_bp:]
        print(final_str)
        print("--------------------------------")
        print("")

prot_seq = Seq(final_str).translate()
print()
print("Protein translated sequence:")
print(prot_seq.replace("*",""))