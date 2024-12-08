class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        # https://docs.python.org/ja/3/library/heapq.html#heapq.heapify
        # リストnumsをヒープ（優先度付きキュー）に変換します。これにより、最小の要素が常に先頭に来るようになります。
        heapq.heapify(self.nums)
        
        # init 
        # ヒープのサイズがkを超えている場合、最小の要素を取り除くためにheapq.heappop(self.nums)を使用します。これによって、ヒープにはk個の最大要素のみが残ります。
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            # pop を行い、 heap から最小の要素を返します。ヒープ不変式は保たれます。
            heapq.heappop(self.nums)

        #pop せずに最小の要素にアクセスするには、 heap[0] を使ってください。
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)