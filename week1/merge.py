"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    temp_line = [0]*len(line);
    index_m = 0
    for num in line:
    	if num != 0:
    		temp_line[index_m] = num
    		index_m += 1
    for index, num in enumerate(temp_line):
    	if index < (len(temp_line)-1) and num == temp_line[index+1]:
    		temp_line[index] += num
    		temp_line[index+1] = 0
    mergedline = [0]*len(temp_line);
    index_m = 0
    for num in temp_line:
    	if num != 0:
    		mergedline[index_m] = num
    		index_m += 1
    return mergedline

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8] )