# Given an unsorted array of integers, find the length of the longest consecutive elements sequence
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest censecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Time: O(n)
# Memory: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet: set[int] = set(nums)
        longest: int = 0

        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
solution: Solution = Solution()

print(solution.longestConsecutive([100, 4, 200, 1, 3, 2, 5]))