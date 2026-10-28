class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)          # Get the length of the input array
        res = [0] * (2 * n)    # Create a result array of size 2n, initialized with zeros

        for i in range(n):     # Iterate through the input array
            res[i] = nums[i]   # Copy the element to its original position
            res[i + n] = nums[i]  # Copy the same element to the second half

        return res             # Return the concatenated array
#Time Complexity: O(n) — The loop iterates n times, performing constant-time operations in each iteration.

#Space Complexity: O(n) — The result array stores 2n elements, requiring O(2n) = O(n) additional space