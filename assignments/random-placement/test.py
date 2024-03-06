from main import placement

print("2x2 Matrix Tests: ")
print("\n")

#test case with 2x2 map with 4 objects
print("1. 2x2 World with 4 Objects: " + str(placement(4, [[(0,0), (0,1)], 
                                                          [(1,0), (1,1)]])))

# test case with 2x2 map and 2 objects
print("2. 2x2 World with 2 Objects: " + str(placement(2, [[(0,0), (0,1)], 
                                                          [(1,0), (1,1)]])))

# test case with 2x2 map and 2 objects
print("3. 2x2 World with 2 Objects: " + str(placement(2, [[(0,0), (0,1)], 
                                                          [(1,0), (1,1)]])))

print("\n")
print("NxN Matrix Tests (N > 2): ")
print("\n")

#test case with 3x3 map with 4 objects
print("1. 3x3 World with 4 Objects: " + str(placement(4, [[(0,0), (0,1), (0,2)], 
                                                          [(1,0), (1,1), (1,2)], 
                                                          [(2,0), (2,1), (2,2)]])))

#test case with 6x6 map with 8 objects
print("2. 6x6 World with 8 Objects: " + str(placement(8, [[(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)], 
                                                          [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5)], 
                                                          [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5)], 
                                                          [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5)], 
                                                          [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5)], 
                                                          [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]])))

print("\n")
print("Variable Size Matrix Tests: ")
print("\n")

#test case with 1x3 map with 2 objects
print("1. 1x3 World with 2 Objects: " + str(placement(2, [[(0,0), (0,1), (0,2)]])))

#test case with 2x3 map with 3 objects
print("2. 2x3 World with 3 Objects: " + str(placement(3, [[(0,0), (0,1), (0,2)], 
                                                          [(1,0), (1,1), (1,2)]])))

#test case with 2x4 map with 4 objects
print("3. 2x4 World with 4 Objects: " + str(placement(4, [[(0,0), (0,1), (0,2), (0,3)], 
                                                          [(1,0), (1,1), (1,2), (1,3)]])))

#test case on a 3x4 map with 3 objects
print("4. 3x4 World with 3 Objects: " + str(placement(3, [[(0,0), (0,1), (0,2), (0,3)], 
                                                          [(1,0), (1,1), (1,2), (1,3)], 
                                                          [(2,0), (2,1), (2,2), (2,3)]])))

#test case with 3x6 map with 9 objects
print("5. 3x6 World with 9 Objects: " + str(placement(9, [[(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)], 
                                                          [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5)], 
                                                          [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5)]])))

