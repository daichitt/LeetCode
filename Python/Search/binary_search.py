class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid # index
            if nums[mid] < target:
                low = mid + 1    # targetが大きいので右側を探索
            else:
                high = mid - 1

        return low

if __name__ == '__main__':
    solution = Solution()
    res = solution.searchInsert([2,4,6], 6)
    print("結果 is " + str(res))