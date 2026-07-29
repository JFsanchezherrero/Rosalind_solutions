import numpy as np

print("Input the number of months to pass and the amount of months each rabbit lives")
n_months=int(input())
m_months=int(input())

col_matrix = list(range(0, m_months))
#col_matrix.append('Exitus')
print("Age rabbits: ")
print(col_matrix)

print("")
print("Months: ")
row_matrix = list(range(1, n_months+1))
print(row_matrix)
print("----------------------------")


## important to set dtype="int64"
np_rabbits = np.zeros([len(row_matrix), len(col_matrix)],  dtype="int64")
print()
print(np_rabbits)
print()
debug_flag = 1
print("Length row:" + str(len(np_rabbits)))
for row in range(len(np_rabbits)):

    ## initialize month 1 with 1 pair
    if row==0:
        ## initialize
        np_rabbits[0][0]=1
        continue

    ################################
    ## Print debug messages
    ################################
    if debug_flag:
        print("----------------------------")
        print("Row " + str(row+1))
        print("Length list colums:" + str(len(np_rabbits[row])))
        print("----------------------------")

    for i in range(len(np_rabbits[row])):
        if (i==0):
            np_rabbits[row][i] = sum([np_rabbits[row-1][i] for i in range(1, len(np_rabbits[row]))])

        if (i>0):
            np_rabbits[row][i] = np_rabbits[row-1][i-1]

        ################################
        ## Print debug messages
        ################################
        if debug_flag:
            print("i=" + str(i) + " " + str(np_rabbits[row][i]))

    print()

print()
print(np_rabbits)
print()

## total number of rabbits
print("Total number of rabbits after n months")
print(int(np_rabbits[-1].sum()))
print(int(sum(np_rabbits[-1])))