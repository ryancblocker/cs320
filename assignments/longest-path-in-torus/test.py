from main import longest_path

matrix = [5, 10, 20], [3, 8, 5], [1, 4, 15]
answer1 = "[(2,0),(1,0),(1,2),(1,1),(0,1),(0,2),(2,2)]"

matrix_2 = [9, 9, 9, 5], [9, -1, 9, 6], [9, 9, 9, 7], [1, 2, 3, 4]
answer2 = "[(3,0),(3,1),(3,2),(3,3),(0,3),(1,3),(2,3),(2,2) or (2,0)]"

testoutput = str(longest_path(matrix))

print("Answer: " + answer1)
print("Test:   " + testoutput)

if (answer1 == testoutput):
    print("Correct!")
else:
    print("Incorrect")

testoutput2 = str(longest_path(matrix_2))

print("Answer: " + answer2)
print("Test:   " + testoutput2)

if (answer2 == testoutput2):
    print("Correct!")
else:
    print("Incorrect")