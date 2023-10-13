# The algorithm specified in question does not require the elements of the superset to be known
# For the purpose of this program, the cardinality of the set will be asked 
cardinalityA = int(input("Enter number of elements in Set A: "))

# The question requires the bitstrings of two subsets of baseSet

# NOTE TO SELF - Len function only works on string - so convert other data types to str to use len function
subsetbx = input("Enter subsetbx: ")

while len(str(subsetbx)) != cardinalityA:
    subsetbx = input("Enter the correct number of members - The subset must equal the cardinality of the baseSet: ")

# Repeat same for subset Y
subsetby = input("Enter subsetby: ")

while len(str(subsetby)) != cardinalityA:
    subsetby = input("Enter the correct number of members - The subset must equal the cardinality of the baseSet: ")
    
print("Given the finite set A - subsetbx\subsetby for  bx belongs to A and by belongs to A")

# bxDy (bx DIFFERENCE by) is the set which have the members of x\y
bxDy = ""
# for loop i < cardinality of set A 
for i in range(0,cardinalityA):
    # Another way to think of difference is as bx-by
    # any element of bx-by must be belong to bx and does not belong to by
    if(subsetbx[i] == '1' and subsetby[i] == '0'):
        bxDy = bxDy + '1'
    else:
        bxDy = bxDy + '0'
    
print("Bx\y: " + bxDy)

