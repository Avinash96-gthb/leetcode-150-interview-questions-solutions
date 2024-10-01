class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last=len(s)-1
        count = 0
        while s[last]==" " and last >= 0:
            last -= 1
        while s[last] != " " and last >= 0:
            count += 1
            last -= 1
        return count
