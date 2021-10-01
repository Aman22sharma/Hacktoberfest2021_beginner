#AUTHOR: Pornpimol Kaewphing
#Python3 Concept: Twosum in Python
#GITHUB: https://github.com/gympohnpimol

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = []
        for i in range(0, len(nums)):
            item = target - nums[i]
            nums[i] = "done"
            if item in nums:
                ls.append(i)
                ls.append(nums.index(item))
        return ls