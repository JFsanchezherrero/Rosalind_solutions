# Given a file, read it and get information
import sys

# input file provided as sys.argv[1] element
with open (sys.argv[1], "r") as file:
    line =file.readline().split()
    k, m, n= [int(n) for n in line]
file.close()

## create a function to ease the computation
# k  = number of homozygous dominant organisms
# n = number of heterozygous organisms
# m  = number of homozygous recessive organisms
def mendel_iprb(k, m, n):
    from scipy.special import comb
    n_ind = k+m+n
    print("Total individuals: ", n_ind)

    # total population of alleles taken into account 
    # 4 genotypes in each mating, and 2 individuals taken
    pop_total = comb(n_ind, 2)
    print("Total combinations of alleles: ", pop_total)
    print("----------\n")

    # dominant organisms         
    ## add the probability of each to produce dominant genotypes: 
    # AAxAA:1; AAxAa=1; AAxaa=1; 
    # AaxAa=3/4; Aaxaa= 2/4 and 
    # aaxaa:0/4
    validCombos = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)

    print("Dominant organisms: ", validCombos)

    # probability for dominant organisms
    phom = validCombos/pop_total
    print("Dominant Probability: " + format(phom, ".2%"))
    print("----------\n")

    # Prob. dominant organisms + prob. recessive organisms equals 1
    # let's check that:
    rec_total = .5*n*m + .75*comb(m, 2) + .5*comb(n, 2) 
    print("Recursive organisms: ", rec_total)

    prec = rec_total/pop_total
    print("Recursive Probability: " + format(prec, ".2%"))

    print("----------\n")
    if(1 - prec == phom):
        print("Prob. dominant organisms + prob. recessive organisms equals 1")
        print("Correct!")



    return(phom)

print(mendel_iprb(k, m, n))