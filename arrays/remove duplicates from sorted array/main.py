class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # Initialize k to keep track of the next position for a unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:  # If the current element is different from the previous unique element
                nums[k] = nums[i]  # Move the current unique element to the appropriate position
                k += 1

        return k
