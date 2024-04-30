from main import *

def test_btree():
    print("Creating BTree...")
    bt = BTree()

    # Test 1: Insertion into an empty tree
    print("Test 1: Inserting into an empty tree...")
    bt.insert(10)
    assert bt.traverse() == (10,), f"Expected (10,), but got {bt.traverse()}"

    # Test 2: Deleting from an empty tree
    print("Test 2: Deleting from an empty tree...")
    bt.delete(10)
    assert bt.traverse() == None, f"Expected None, but got {bt.traverse()}"

    # Test 3: Insertion of multiple elements
    print("Test 3: Inserting multiple elements...")
    elements = [15, 10, 20, 5, 12, 30, 25, 1]
    for e in elements:
        bt.insert(e)
    expected = (1, 5, 10, 12, 15, 20, 25, 30)
    assert bt.traverse() == expected, f"Expected {expected}, but got {bt.traverse()}"

    # Test 4: Deletion with redistribution
    print("Test 4: Deletion with redistribution...")
    bt.delete(20)
    bt.delete(25)
    expected = (1, 5, 10, 12, 15, 30)
    assert bt.traverse() == expected, f"Expected {expected}, but got {bt.traverse()}"

    # Test 5: Contains
    print("Test 5: Checking contains...")
    assert bt.contains(15) == True, "Expected True for contains(15)"
    assert bt.contains(20) == False, "Expected False for contains(20)"

    # Test 6: Large scale test
    print("Test 6: Large scale test...")
    bt2 = BTree()
    for i in range(100, 200):
        bt.insert(i)
    for i in range(150, 170):
        bt.delete(i)
    if not bt.contains(160):
        print("160 successfully deleted.")
    else:
        print("Error: 160 not deleted.")

    print("All tests completed.")


test_btree()


