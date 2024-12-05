class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0 #init 
        for num in nums:
            if num != 0:
                nums[left] = num
                left = left + 1 # go to next index

        for num in range(left, len(nums)):
            nums[num] = 0 # put 0p

        