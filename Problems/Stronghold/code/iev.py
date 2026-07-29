import sys

# input file provided as sys.argv[1] element
with open(sys.argv[1]) as f:
  counts_str = f.read().strip()


list_of_couples = counts_str.split()
genotypes = {"g0" : ["AA-AA", 1], 
             "g1" : ["AA-Aa", 1], 
             "g2" : ["AA-aa", 1], 
             "g3" : ["Aa-Aa", 0.75], 
             "g4" : ["Aa-aa", 0.5], 
             "g5" : ["aa-aa", 0]
             }

## debugging purposes
for i in range(len(list_of_couples)):
    print("Number of couples: " + str(list_of_couples[i]))
    print("Genotypes: " + genotypes["g"+str(i)][0] +" & Prob.:" + str(genotypes["g"+str(i)][1]))
    print()


## 
print("Total Expected offsrping:")
print(sum([genotypes["g"+str(i)][1]*int(list_of_couples[i]) for i in range(len(list_of_couples))])*2)