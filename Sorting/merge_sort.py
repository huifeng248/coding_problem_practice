def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[0: len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        # recursion 
        x = merge_sort(left_arr)
        merge_sort(right_arr)
        
        # merge-- conbination 
        i = 0
        j = 0 
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if x[i] < right_arr[j]:
                arr[k] = x[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # merge_sort(x)
        # merge_sort(right_arr)
        while i < len(x):
            arr[k] = x[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            
    return arr
            
        



arr1 = [2,3, 1, -1, 5]
arr2 = [2,3, 1, -1, -5, 7]

print(merge_sort(arr1))
print(merge_sort(arr2))
