from main import mergesort

print("EDGE CASES")
print("1. original: None")
print("      final: " + str(mergesort(None))) # should be None
print("2. original: [5]")
print("      final: " + str(mergesort(5))) # should be None
print("3. original: []")
print("      final: " + str(mergesort([]))) # should be []
print("\n")
print("ODD-LENGTHS")
print("3. original: [9, 5, 8]")
print("      final: " + str(mergesort([9, 5, 8]))) #should be [5, 8, 9]
print("4. original: [100, 5, 8, 10, 9]")
print("      final: " + str(mergesort([100, 5, 8, 10, 9]))) #should be [5, 8, 9, 10, 100]
print("\n")
print("EVEN-LENGTHS")
print("5. original: [100, 350, 1500, 8]")
print("      final: " + str(mergesort([100, 350, 1500, 8]))) #should be [8, 100, 350, 1500]
print("6. original: [100, 350, 1500, 8, 200, 850, 4500, 75]")
print("      final: " + str(mergesort([100, 350, 1500, 8, 200, 850, 4500, 75]))) #should be [8, 75, 100, 200, 350, 850, 1500, 4500]
print("\n")
print("DUPLICATES")
print("7. original: [5, 8, 9, 9, 4, 1, 6, 6, 6]")
print("      final: " + str(mergesort([5, 8, 9, 9, 4, 1, 6, 6, 6]))) #should be [1, 4, 5, 6, 6, 6, 8, 9]
print("8. original: [5, 8, 8, 9, 10]")
print("      final: " + str(mergesort([5, 8, 8, 9, 10]))) #should be [5, 8, 8, 9, 10]
print("\n")

# def sort_list(list):
    #     sorted_list.append(list[0])
    #     for i in range(1, len(list)):
    #         print(sorted_list)
    #         if (list[i] >= sorted_list[-1]):
    #             sorted_list.append(list[i]) 
    #         elif (list[i] < sorted_list[0]):
    #             sorted_list.insert(0, list[i]) 
    #         else:
    #             for j in range(0, len(sorted_list)):
    #                 if(list[i] > sorted_list[j]) and (list[i] < sorted_list[j + 1]):
    #                     sorted_list.insert(j, list[i])
    #                     break
    # 