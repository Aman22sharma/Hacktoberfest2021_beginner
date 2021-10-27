class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        dic = {}
        while end < len(s):
            if s[end] in dic and dic[s[end]] >= start:
                start = dic[s[end]] + 1
            max_len = max(max_len, end - start + 1)
            dic[s[end]] = end
            end += 1
        return max_len
