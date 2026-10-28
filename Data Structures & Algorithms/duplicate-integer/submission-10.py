class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # TC: O(n log n) — Sorting the array

        for i in range(1, len(nums)):  # TC: O(n) — Loop runs at most n-1 times
            if nums[i] == nums[i - 1]:  # TC: O(1) — Compare adjacent elements
                return True

        return False

    # TC Calculation:
    # Sorting: O(n log n)
    # Loop: O(n)
    # Total: O(n log n) + O(n) = O(n log n)

    # SC Calculation:
    # Sorting may use O(n) auxiliary space in Python's Timsort.
    # Loop uses O(1) extra space.
    # Total auxiliary SC: O(n)

        