// AUTHOR: Ananya
// Python3 Concept:removal of duplicates
// GITHUB: https://github.com/ananya321

//Add your python3 concept below
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
        
