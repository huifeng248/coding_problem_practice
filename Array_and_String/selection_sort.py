def selection_sort(arr):
    for i in range(0, len(arr)):
        print("circle i+++++", i)
        print()
        # min = arr[i]
        # min_index = i 
        for j in range(i+1, len(arr)):
            print("circle j-------", j)
            if arr[j] < arr[i]:
                print(i,"iiiii", arr[i])
                print(j,"JJJJ", arr[j])
                
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
    return arr
            


# arr1 = [3, 2, 2, 4]
arr2 = [0, 2, -1, -3, -5]

# print(selection_sort(arr1))
print(selection_sort(arr2))

# time complexity: n square
# space complexity: 
# Worst Case Time Complexity is: O(N2)
# Average Case Time Complexity is: O(N2)
# Best Case Time Complexity is: O(N2)
# Space Complexity: O(1)