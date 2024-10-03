class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        maxlenght=0
        uniquechar=set()

        for right in range(n):
            if s[right] not in uniquechar:
                uniquechar.add(s[right])
                maxlenght = max(maxlenght,right-left+1)
            else:
                while s[right] in uniquechar:
                    uniquechar.remove(s[left])
                    left+=1
                uniquechar.add(s[right])
                maxlenght = max(maxlenght,right-left+1)

        return maxlenght
        
