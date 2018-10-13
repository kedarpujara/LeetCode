"""
Kedar Pujara
4/18/18

So here is how I approached the problem and my overall thought process (sorry it's long): 

1. Make some assumptions
   - If the following numbers are present: 00, 30, 40, 50, 60, 70, 80, 90, return empty array   
   - Can only be a string of digits 

2. Lay out Base cases 
   - No digits
   - Only one digit
   - If that one digit is a 0 
   - If that one digit is an empty string 

3. Initialize my map at the empty string and 1 (first number in the input number)
   - "" -> [""] 
   - "1" -> ["First number of input string"]
   - Herein begins the dynamic programming 

4. Iterate one number at a time in the given input number (if it was 12346, start with 2, then 3, then 4, then 6)
   - Look at double digit numbers
   - Check if they satisfy the conditions to be a double digit alphabet (10-26)
   - If valid double digit, then append that letter to the end of each letter in the array for the 
   	 string that came two before it
   - If it is not a valid double digit, say 34 in this instance, you want to simply append "4" to the end of 
     each value for the key of the string before it 
   - Check for special cases 

5. Special Cases 
   - I have already mentioned many above
   - 10/20 special cases since the 0 cannot stand alone 
   - You also cannot split up 01-09
   - Just test a lot of numbers to make sure I get all edge cases 
   - Numbers used are in the main method

6. Analytics
   - This runs in O(len(num) * m)), 
     where num is the input string, ('1123' -> 4)
     m is the max of all iterations leading up to possib[num], ('1123' -> 5)
     and possib is the dictionary holding the possible outputs of alphabetical characters the string can generate 

7. Research
	I did not use google for this. I initially tried it entirely from scratch and by hand on my notebook to understand
	the patterns. And then I collaborated with a friend to help me solidify my reasoning and thought process as well as 
	make sure I wasn't missing any edge cases. 

8. Robustness 
	I believe it is robust because it can handle all possibilities and every
	input results in a valid state. I have done thorough error checking and this program
	can handle any input for any variable and it will return a response with no errors

"""


def AlphabetCombos(num):
	# Check if input is string. If it is, check if string is all digits. If not, return []
	if isinstance(num, str) == False:
		print("Invalid input, try a different one!")
		return []
	elif num.isdigit() == False:
		print("Invalid input, try a different one!")
		return []		


	alphabet = Alphabet() #Initialize alphabet
	possib = {}  #dictionary to keep track of dynamic programming. Will return possib[num]
	doubleDigit = ""


	### STEP 2. Base Cases ###
	if(len(num) == 0 or (not num) or num[0] == '0' or num=='0'*len(num)):
		print("Invalid input, try a different one!")		
		return []
	
	### STEP 3. Initialize ###
	possib[""] = [""]
	possib["1"] = alphabet[num[0]]
		

	### STEP 4. Iterate ###
	for i in range(2, len(num)+1):
		doubleDigit = num[i-2:i] # Double digit value we are assessing 
		fullStr = num[:i] #Full string at the index
		prev = num[:i-1] #Previous full string
		prev2 = num[:i-2] #Full string from two keys before 

		
		if doubleDigit[1] == "0":
			# For numbers 10 or 20
			if doubleDigit[0] == "2" or doubleDigit[0] == "1":
				curr = [i+alphabet[doubleDigit] for i in possib[prev2]]
			# For numbers 00, 30, 40, 50, 60, 70, 80, 90, just return empty array
			else:
				print("Invalid input, try a different one!")		
				return []


		else:
			#Adding the single digits to the previous string 
			curr = [i+alphabet[doubleDigit[1]] for i in possib[prev]]
			# If valid double digit, adding double digit alphabet full string two keys before
			if '11' <= doubleDigit <= '26':
				curr.extend([i+alphabet[doubleDigit] for i in possib[prev2]])

		# Add the appended array 
		possib[fullStr] = curr
					
	print possib[num]
	return possib[num]


### Setting up the alphabet map ####
def Alphabet():
	alphabet = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e",
			    "6": "f", "7": "g", "8": "h", "9": "i", "10": "j",
			    "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", 
			    "16": "p", "17": "q", "18": "r", "19": "s", "20": "t",
			    "21": "u", "22": "v", "23": "w", "24": "x", "25": "y",
			    "26": "z"}

	return alphabet



def main():
	num = "1123" #Given example ("aabc, "kbc", "alc", "aaw", "kw")
	num1 = "203" #Only be two letters (20 -> t, 3-> c)
	num2 = "2030" #Should fail
	num3 = "0123" #Should fail, leading zero
	num4 = "10238" #should be all good (2 possibilities)
	num5 = "123810" #Should be all good
	num6 = "1238100" #Should fail due to leading zeros 
	num7 = "90" #Should fail. 90 not in alphabet
	num8 = "909" #Should fail, 90 or 0 not in alphabet
	num9 = "01"
	AlphabetCombos(num)


main()
