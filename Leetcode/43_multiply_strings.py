class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2 == "0":
            return "0"
        len_1, len_2 = len(num1), len(num2)
        res = [0] * (len_1+len_2)
        
        num_1 = num1[::-1]
        num_2 = num2[::-1]

        for i, digit_1 in enumerate(num_1):
            for j, digit_2 in enumerate(num_2):
                 # The number of zeros from multiplying to digits depends on the place
                # of digit2 in second_number and the place of the digit1 in first_number.
                
                num_zeros = i + j
                # print("digit1", digit_1, "2digit", digit_2)

                # The digit currently at position numZeros in the answer string
                # is carried over and summed with the current result
                carry = res[num_zeros]
                multi = int(digit_1) *int(digit_2) + carry

              # Set the ones place of the multiplication result.
              # update the digit in this position
                res[num_zeros] = multi % 10
                # print(num_zeros+1, res[num_zeros+1], "multi", multi, "res", res, "carry", carry)

                 # Carry the tens place of the multiplication result by 
                # adding it to the next position in the answer array.
                res[num_zeros+1] += multi//10
                # print("res", res)

        if res[-1] == 0:
            res.pop()
            
        return "".join(str(num) for num in reversed(res))

#Time complexity: O(M⋅N).
#space complexity: O(M+N)