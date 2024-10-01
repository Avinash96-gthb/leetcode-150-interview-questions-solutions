class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len=len(needle)
        i=0
        while i+needle_len <= len(haystack):
            if needle==haystack[i:i+needle_len]:
                return i
            else:
                i+=1
        return -1
