int_given=6
list_num=list(range(1,int_given+1))
print(list_num)

from itertools import permutations

count_perm = 0
perm_str = ""
perm = permutations(list_num)

for i in perm:
    count_perm +=1
    print(i)
    perm_str += " ".join(map(str, i))+"\n"

print("\n-----------------------------------------------------\n")

## print ouput
print(count_perm)
print(perm_str)