# Given an array of integers that is already sorted in ascending order. Find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such they add up to the target, where index1 must be less than index2

# Input: numbers = [1, 3, 4, 5, 7, 10, 11], target = 9
# Output: [2, 3]
# Explanation: The sum of 4 and 5 is 9. Therefore index1 = 2, index2 = 5


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        leftPointer, rightPointer = 0, len(numbers) - 1

        while leftPointer < rightPointer:
            currentSum = numbers[leftPointer] + numbers[rightPointer]

            if currentSum > target:
                rightPointer -= 1
            elif currentSum <target:
                leftPointer += 1
            else:
                return [leftPointer, rightPointer]
            
        return []

solution: Solution = Solution()

print(solution.twoSum(numbers=[1, 3, 4, 5, 7, 10, 11], target=9))