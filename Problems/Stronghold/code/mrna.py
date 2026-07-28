from Bio.Data.CodonTable import unambiguous_dna_by_id
import sys

## read proteic sequence
with open(sys.argv[1]) as f:
  prot_string = f.read().strip()

###############################################
# Load the standard genetic code (ID 1)
###############################################
table = unambiguous_dna_by_id[1]

# Invert forward_table (codon -> aa) 
# to map amino acid -> list of codons
aa_to_codons = {}
for codon, aa in table.forward_table.items():
    aa_to_codons.setdefault(aa, []).append(codon)

## add stop codons
aa_to_codons['*'] = table.stop_codons

## add start codons aa_to_codons['^'] = table.start_codons
###############################################

## add stop codon
prot_seq_r = prot_string + '*'

## get possibilities
listOfCodons = []
for i in prot_seq_r:
    codons = aa_to_codons.get(i)
    print(codons)
    listOfCodons.append(codons)

total_count = 1
for i in listOfCodons:
    total_count *= len(i)

print(total_count % 1000000)