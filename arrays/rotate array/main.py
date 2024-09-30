class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k > len(nums):
            k -= len(nums)
        point = (len(nums)-1)-k
        temp1 = nums[0:point+1]
        temp2 = nums[point+1:len(nums)]
        print(temp2)
        nums[:] = temp2 + temp1
        return nums

        
