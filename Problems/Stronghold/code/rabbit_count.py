import sys

string2check = sys.argv[1]
list2check = string2check.split(" ")
month2check = int(list2check[0])
num_offSpring2check = int(list2check[1])


def getRabbits(starting_pairs = 1, num_offSpring=0, month_to_check=0):

    if month_to_check<3:
        return(starting_pairs)
    
    if month_to_check==3:
        return(starting_pairs + num_offSpring)

    if month_to_check>3:
        total_n1= getRabbits(starting_pairs, num_offSpring, month_to_check-1)
        total_n2= getRabbits(starting_pairs, num_offSpring, month_to_check-2)

        total_n = total_n1 + total_n2*num_offSpring 

        return(total_n)
    

## call the function
print(getRabbits(starting_pairs=1, 
                 num_offSpring=num_offSpring2check,  
                 month_to_check= month2check))