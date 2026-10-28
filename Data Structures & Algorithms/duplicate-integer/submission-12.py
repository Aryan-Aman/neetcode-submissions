class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()                # SC: O(n) — Stores unique elements

        for n in nums:               # TC: O(n) — Iterates through n elements
            if n in seen:            # TC: O(1) average — Checks if element exists
                return True          # Duplicate found

            seen.add(n)               # TC: O(1) average — Adds element to set

        return False                  # No duplicates found

# TC Calculation:
# Loop runs n times: O(n)
# Set lookup and insertion: O(1) average per operation
# Total TC: O(n) average

# SC Calculation:
# Set can store up to n unique elements
# Total SC: O(n)