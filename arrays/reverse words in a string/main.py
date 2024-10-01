class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        words.reverse()
        reversed_s=' '.join(words)
        return reversed_s
        
