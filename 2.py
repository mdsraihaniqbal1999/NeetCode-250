from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        # Check for consecutive duplicates
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False

# Input method
n = int(input("Enter the number of elements: "))
arr = [int(x) for x in input("Enter the array elements: ").split()[:n]]
print(f"The array elements are: {arr}")

# Create an instance of the Solution class
solution = Solution()

# Call the hasDuplicate method and print the result
result = solution.hasDuplicate(arr)
print(f"Does the array have duplicates? {result}")
