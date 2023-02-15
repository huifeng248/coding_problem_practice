class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # solution one 
        # convert the array form interger into int
        # add them and turn the sum into array form
        
        sub_total = 0 
        i = len(num)-1
        j = 0
        while j < len(num):
            digit = num[j] * (10**i)
            sub_total += digit
            j+= 1
            i -= 1 
        
        
        sub_total += k 

        res = list(str(sub_total))
        print("res", res)
        return [int(i) for i in res]

        # time complexity is O(n), n is the max(len(num), len(sum))
        # space complexity is O(n), n is the max(len(num), len(sum))

        # Solution two 

        # num[-1] += k
        # carry = 0
        # part_one = []
        # for i in range(len(num)-1, -1, -1):
        #     # print("i@@", i, "digit", num[i], num)
        #     carry, remainder = divmod(num[i], 10)
        #     num[i] = remainder
        #     # print("i##", i, num[i], "remainder", remainder, num)
            
        #     if i:  # why if i >= 0 does not work
        #         print("1~~~", "i", num[i-1])
        #         num[i-1] += carry
        # if carry:
        #     part_one = [int(i) for i in str(carry)]

        # print("part_one", part_one, "num", num)
        # return part_one + num


            

        
      




