from main import longest_path

matrix = [[5, 10, 20], [3, 8, 5], [1, 4, 15]]
answer1 = "[(2, 0), (1, 0), (1, 2), (1, 1), (0, 1), (0, 2)]"

matrix_2 = [[9, 9, 9, 5], [9, -1, 9, 6], [9, 9, 9, 7], [1, 2, 3, 4]]
answer2a = "[(3, 0), (3, 1), (3, 2), (3, 3), (0, 3), (1, 3), (2, 3), (2, 0)]"
answer2b = "[(3, 0), (3, 1), (3, 2), (3, 3), (0, 3), (1, 3), (2, 3), (2, 2)]"

matrix_3 = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12], [16, 15, 14, 13]]
answer3 = "[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0)]"


testoutput = str(longest_path(matrix))

print("Answer: " + answer1)
print("Test:   " + testoutput)

if (answer1 == testoutput):
    print("Correct!")
else:
    print("Incorrect")

testoutput2 = str(longest_path(matrix_2))

print("Answer: " + answer2a)
print("Test:   " + testoutput2)

#if either answer2a or answer2b is equal to the testoutput2, print correct
if (answer2a == testoutput2) or (answer2b == testoutput2):
    print("Correct!")
else:
    print("Incorrect")

testoutput3 = str(longest_path(matrix_3))

print("Answer: " + answer3)
print("Test:   " + testoutput3)

if (answer3 == testoutput3):
    print("Correct!")
else:
    print("Incorrect")
    
# def longest_path(torus):

#     if torus is None or not torus[0]:
#         return []
    
#     num_rows = len(torus)
#     num_cols = len(torus[0])

#     def is_valid(x, y, value):
#         return torus[x][y] > value

#     def depth_first_search():
#         longest_path = []

#         def dfs(node, current_path):
#             nonlocal longest_path
            
#             if len(current_path) > len(longest_path):
#                 longest_path = current_path[:]

#             for neighbor in get_neighbors(node):
#                 x, y = neighbor
#                 if is_valid(x, y, torus[node[0]][node[1]]):
#                     dfs(neighbor, current_path + [neighbor])

#         for i in range(num_rows):
#             for j in range(num_cols):
#                 dfs((i, j), [(i, j)])

#         return longest_path

#     def get_neighbors(node):
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         result = []
    
#         for direction in directions:
#             x = (node[0] + direction[0]) % num_rows
#             y = (node[1] + direction[1]) % num_cols
#             result.append((x, y))

#         return result

#     return depth_first_search()
