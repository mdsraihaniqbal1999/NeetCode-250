from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1 = nums
        nums_res = nums + nums1
        return nums_res

# Input method
n = int(input("Enter the number of elements: "))
arr = [int(x) for x in input("Enter the array elements: ").split()[:n]]
print(f"The array elements are: {arr}")

# Create an instance of the Solution class
solution = Solution()

# Call the getConcatenation method and print the result
result = solution.getConcatenation(arr)
print(f"The concatenated array is: {result}")
