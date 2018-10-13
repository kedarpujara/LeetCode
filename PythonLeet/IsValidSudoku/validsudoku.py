# matrix = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

# matrix = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

# matrix = [["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]
#
# matrix = [[".",".","4",".",".",".","6","3","."],
# [".",".",".",".",".",".",".",".","."],
# ["5",".",".",".",".",".",".","9","."],
# [".",".",".","5","6",".",".",".","."],
# ["4",".","3",".",".",".",".",".","1"],
# [".",".",".","7",".",".",".",".","."],
# [".",".",".","5",".",".",".",".","."],
# [".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".","."]]
#
# [".",".",".",".","5",".",".","1","."],
# [".","4",".","3",".",".",".",".","."],
# [".",".",".",".",".","3",".",".","1"],
# ["8",".",".",".",".",".",".","2","."],
# [".",".","2",".","7",".",".",".","."],
# [".","1","5",".",".",".",".",".","."],
# [".",".",".",".",".","2",".",".","."],
# [".","2",".","9",".",".",".",".","."],
# [".",".","4",".",".",".",".",".","."]]

# matrix = [["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]

matrix = [[".",".",".",".","5",".",".","1","."], 
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]

#print(matrix[0:3])
def valid(matrix):

    valid = False

    # #valid horizontal
    # valid = valid_horizontal(matrix)
    # print valid

    # #valid vertical
    # dict = {}
    # valid = valid_vert(matrix,0,dict)
    # print valid

    #valid squares
    valid = valid_squares(matrix)
    print valid

    return valid

def valid_horizontal(matrix):
    for line in matrix:
        if(valid_line(line) == False):
            return False
    return True

def valid_vert(sudoku,i,dict):
    line_number = 1
    for i in range(9):
        for line in sudoku:
            #print line[i]
            if line[i] in dict:
                return False
            else:
                if line[i] != '.':
                    dict[line[i]] = 1
            line_number = line_number + 1
        print(dict)
        dict = {}
    return True
    # if i < 8:
    #     i = i+1
    #     valid_vert(sudoku,i,dict)
    # else:
    #     print("Here")
    #     return True


def valid_line(line):
    dict = {}
    for i in range(len(line)):
        if line[i] in dict:
            return False
        else:
            if line[i]!= ".":
                dict[line[i]] = 1


def valid_squares(matrix):
    #if counter gets to 2, reset all dictionaries
    dict1 = {}
    dict2 = {}
    dict3 = {}
    i = 0
    counter = 0

    for line in matrix:
    	for i in range(9):
	        if i <= 2 and i >= 0:
	            #add to first dictionary
	            if line[i] in dict1:
	            	print(line[i])
	            	print(i)
	                return False
	            else:
	            	if line[i] != ".":
		                dict1[line[i]] = 1
	        elif i <= 5 and i >= 3:
	            #add to second dictionary
	            if line[i] in dict2:
	            	print(line[i])
	            	print(i)            	
	                return False
	            else:
	            	if line[i] != ".":
	                	dict2[line[i]] = 1
	        elif i <= 8 and i >= 6:
	            #add to third dictionary
	            if line[i] in dict3:
	                return False
	            	print(line[i])
	            	print(i)                
	            else:
	            	if line[i] != ".":
	                	dict3[line[i]] = 1
		print(dict3)

        counter = counter+1
        if counter == 3:
        	print("hello")
        	counter = 0
        	dict1 = {}
        	dict2 = {}
        	dict3 = {}
    return True
print(valid(matrix))

# def valid_vertical(sudoku,i, dict):
#     for j in range(9):
#         if sudoku[i][j] in dict:
#             return False
#         else:
#             if sudoku[i][j] != '.':
#                 dict[sudoku[i][j]] = 1
#
#         if j == 8:
#             dict = {}
#     if i < 9:
#         i = i+1
#         valid_vertical(sudoku,i,dict)
#     else:
#         return True




def valid_threes(sudoku, i, j):
    if(i > 8):
        i = 0
        j = j+2
    curr_square = matrix[i:i+2,j:j+2]
    if(square_helper(curr_square) == False):
        return False
    i = i+2
    valid_threes(sudoku,i,j)
    return True

def square_helper(sudoku):
    dict = {}
    for i in range(3):
        for j in range(3):
            if sudoku[i,j] in dict:
                return False
            else:
                if sudoku[i,j] != ".":
                    dict[sudoku[i,j]] = 1
    return True
