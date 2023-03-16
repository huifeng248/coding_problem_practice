# brute force

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         basket = set()
#         max_count = 0
#         for i in range(len(fruits)):
#             for j in range(i, len(fruits), 1):
#                 # print("basket", basket)
#                 if len(basket) == 2 and fruits[j] not in basket:
#                     basket = set()
#                     break
#                 basket.add(fruits[j])

#                 max_count = max(j -i+1, max_count)
        
#         return max_count
# time complexity: O(N^2)
# space complexity: O(1)

#sliding window: the size is not shrinking
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         # Hash map 'basket' to store the types of fruits.
#         basket = {}
#         left = 0
        
#         # Add fruit from the right index (right) of the window.
#         for right, fruit in enumerate(fruits):
#             print("left", left, "right", right, "basket", basket)
#             basket[fruit] = basket.get(fruit, 0) + 1

#             # If the current window has more than 2 types of fruit,
#             # we remove one fruit from the left index (left) of the window.
#             if len(basket) > 2:
#                 basket[fruits[left]] -= 1

#                 # If the number of fruits[left] is 0, remove it from the basket.
#                 if basket[fruits[left]] == 0:
#                     del basket[fruits[left]]
#                 left += 1
        
#         # Once we finish the iteration, the indexes left and right 
#         # stands for the longest valid subarray we encountered.
#         return right - left + 1

# [[1,2, 0, 0, 0, 0, 3,2,2]
# basket = {1:1, 2:1, 0:1 }  


# optimal solution # sliding window: the left is shrinking to the right 
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 0:
            return 0
        # We use a hash map 'basket' to store the number of each type of fruit.
        basket = {}
        right = left = 0
        max_count = 0

        while right < len(fruits):
            # Add fruit from the right index (right) of the window.
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # If the current window has more than 2 types of fruit,
            # we remove fruit from the left index (left) of the window,
            # until the window has only 2 types of fruit.
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            # Update max_picked.
            right += 1
            max_count = max(max_count, right - left)


        return max_count 

# time complexity: O(N)
# space complexity: O(1)
                




