class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        result=""
        for r in range(numRows):
            incriment=2*(numRows-1)
            for i in range(r,len(s),incriment):
                result+=s[i]
                if (r>0 and r<numRows-1 and i+incriment-2*r < len(s)):
                    result+=s[i+incriment-2*r]
        return result

        
