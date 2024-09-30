class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = 1
        current_num = nums[0]
        count = 1
        for i in range (1,len(nums)):
            if nums[i]==current_num and count < 2:
                nums[size]=nums[i]
                size += 1
                count += 1
            elif nums[i]!=current_num:
                current_num = nums[i]
                count = 1
                nums[size]=nums[i]
                size += 1
        return size
        
