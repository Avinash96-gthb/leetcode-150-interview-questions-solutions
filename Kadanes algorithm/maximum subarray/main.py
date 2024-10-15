class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        l = 0 
        r = 0
        n = len(nums)
        while r<n:
            if(currSum<0):
                l = r
                currSum = 0
            currSum += nums[r]
            maxSum = max(currSum,maxSum)
            r+=1
        return maxSum
