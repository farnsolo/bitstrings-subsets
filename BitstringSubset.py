# Empty list to be filled
test = []

# Ask the user to input set
n = int(input("Enter Number of elements : "))
print("Enter elements - one by one")

 # iterate till range
for i in range(0, n):
    temp = int(input())
    # adding the element
    test.append(temp)
    
    
# Bool that keeps track whether or not the while loop is active
continueLoop = True
# Empty subset list
subset = []


# While loop that allows the user to repeat the sequence
while(continueLoop == True):
    # Reset subset with each iteration
    subset = []
     # User enter bitstring
    bitString = input("Enter Whole Bitstring:")
     
     # iterates through the length of test list - compares contents of Bitstring cell to "1"
    for i in range(0, n):
        if(bitString[i] == "1"):
            # If 1 exists in that index position, then append content of the index position in test list to subset list
            subset.append(test[i])
        
    # Prints out elements of subset
    for z in subset:
         print(z)
        
     # Asks user is they want to repeat sequence
    enterNew = input("Continue? Y/N ")
    if(enterNew == "N" ):
        quit()
    else:
        continueLoop = True

    
        
    
                
                
        
    
                
                
