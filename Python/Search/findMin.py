class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # if nums[mid] <= nums[right]:
            #     right = mid
            # else:
            #     left = mid + 1
            # 右半分がソートされていない場合
            if nums[mid] > nums[right]:
                left = mid + 1
            # 右半分がソートされている場合
            else:
                right = mid
        return nums[left]

        ##[1,2,3,4]
        ##[3,4,5,1,2]
        # left = 3
        # mid = 5
        # right = 2
        # 5 <= 2:

if __name__ == '__main__':
    solution = Solution()
    res = solution.findMin([1, 2, 3])
    print(res)