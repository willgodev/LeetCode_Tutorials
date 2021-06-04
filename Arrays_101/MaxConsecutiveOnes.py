from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longestConsecutive = 0
        currentStreak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentStreak += 1
                if currentStreak > longestConsecutive:
                    longestConsecutive = currentStreak
            else:
                currentStreak = 0
        return longestConsecutive

nums = [1, 1, 0, 1, 1, 1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))
