class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        if volume == 0 :
            return heights
        
        def find_left_min(heights, k):
            i = k
            min_left = (k, heights[k])
            while i> 0:
                if heights[i-1]< heights[i]:
                    i -= 1
                    min_left = (i, heights[i])
                elif heights[i-1] == heights[i]:
                    i -= 1
                    
                else:
                    break
            return min_left

        def find_right_min(heights, k):
            i = k
            min_right = (k, heights[k])
            while i < len(heights)-1:
                if heights[i+1] < heights[i]:
                    i += 1
                    min_right = (i, heights[i])
                elif heights[i+1] == heights[i]:
                    i += 1

                else:
                    break
            return min_right


        left = find_left_min(heights, k)
        left_min_index, left_min_height = left
        right = find_right_min(heights, k)
        right_min_index, right_min_height = right

        if left_min_height < heights[k]:
            left_min_height += 1
            heights[left_min_index] = left_min_height
        elif right_min_height < heights[k]:
            right_min_height += 1
            heights[right_min_index] = right_min_height
        else:
            heights[k] += 1

        return self.pourWater(heights, volume-1, k)

# class Solution:
#     def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
#         while volume > 0:
#             minV = (heights[k], k )
#             index = k

#             for i in range(k-1, -1, -1):
#                 if heights[i] > heights[index]:
#                     break
#                 elif heights[i] < heights[index]:
#                     index = i
#                     if heights[i] <minV[0]:
#                         print(minV, (heights[i],i))
#                         minV= min(minV, (heights[i],i))
#                         print("333", minV)
#             if minV != (heights[k], k ):
#                 heights[minV[1]] += 1
#                 volume -= 1
#                 continue
#             index = k
#             for i in range(k+1, len(heights)):
#                 if heights[i] > heights[index]:
#                     break
#                 elif  heights[i] < heights[index]:
#                     index = i
#                     if heights[i] <minV[0]:
#                         minV = min(minV, (heights[i],i))
#             if minV != (heights[k], k ):
#                 heights[minV[1]] += 1
#                 volume -= 1
#                 continue
#             heights[k]+=1
#             volume -= 1
#         return heights
# print("min", min((2,2), (2,3)))
# # [1,2,3,4,3,2,1,2,3,4,3,2,1]

# 1 [2,2,3,4,3,2,1,2,3,4,3,2,1]


# [4,4,4,4,3,3,3,3,3,4,3,2,1]