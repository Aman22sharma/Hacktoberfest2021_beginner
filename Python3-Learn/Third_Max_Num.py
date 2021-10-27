class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # s = set(nums)
        new_ls = list(set(nums))
        new_ls.sort(reverse=True)
        if len(new_ls) == 1:
            return new_ls[0]
        if len(new_ls) == 2:
            return new_ls[0]
        return new_ls[2]
