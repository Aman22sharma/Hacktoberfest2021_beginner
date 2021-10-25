#AUTHOR: Pornpimol Kaewphing
#Python3 Concept: Twosum in Python
#GITHUB: https://github.com/gympohnpimol

def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    
                    return [i,j]
                else:
                    pass
          
            
