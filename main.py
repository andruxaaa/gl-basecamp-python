
# Global array for hole values 
hole = [ 1, 0, 0, 0, 1, 0, 1, 0, 2, 1 ] 

# Function to return the count 
# of holes in num 
def countHoles(num): 

	holes = 0

	while (num > 0) : 
	
		# Last digit in num 
		d = num % 10

		# Update holes 
		holes = holes + hole[d] 

		# Remove last digit 
		num = num // 10
	
	# Return the count of holes 
	# in the original num 
	return holes 
	
# Driver code 
while True:
    input_str = input("Type integer or q to exit: ")
    try:
        if input_str.lower() == "q":
            break
        input_int = int(input_str)
        print("Number of holes: ", countHoles(input_int))
    except:
        print("Error, input number not integer!!!")

