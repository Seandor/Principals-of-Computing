"""
Merge function for 2048 game.
"""
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    def slide(line):
        """
        Function that slides a single row or column in 2048
        """
        temp_line = [0]*len(line)
        index_s = 0
        for num in line:
            if num != 0:
                temp_line[index_s] = num
                index_s += 1
        return temp_line
    temp_line = slide(line)
    for index, num in enumerate(temp_line):
        if index < (len(temp_line)-1) and num == temp_line[index+1]:
            temp_line[index] += num
            temp_line[index+1] = 0
    mergedline = slide(temp_line)
    return mergedline

# def merge(line):
#     """
#     Function that merges a single row or column in 2048.
#     """
#     temp_line = [num for num in line if num != 0]
#     mergedline = []
#     for index, num in enumerate(temp_line):
#         if index < ( len(temp_line) - 1 ):
#             if num == temp_line[index + 1]:
#                 mergedline.append(num + num)
#                 temp_line[index + 1] = 0
#             elif num != 0:
#                 mergedline.append(num)
#         elif num != 0:
#             mergedline.append(num)
#     while len(mergedline) < len(line):
#         mergedline.append(0)
#     return mergedline

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])