class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            # If there are no prices or only one price, no profit can be made
            return 0

        # Initialize variables
        buy_price = prices[0]  # Set the first price as the initial buy price
        profit = 0  # Start with no profit

        # Iterate over prices starting from the second day
        for p in prices[1:]:
            # Update the buy price if a lower price is found
            buy_price = min(buy_price, p)# 最安値(Buy)を更新
            # Calculate profit and update the maximum profit
            profit = max(profit, p - buy_price) # 最高値(Sell)を更新 sell - buy

        return profit