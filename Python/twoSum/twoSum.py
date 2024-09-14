class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[n] = i