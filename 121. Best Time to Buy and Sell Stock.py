class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        buy = 0
        sell = 1
        maxP = 0
        while(sell < len(prices)):

            if prices[buy] > prices[sell]:
                buy = sell

            else:
                maxP = max(prices[sell] - prices[buy],maxP)
                print("hello")
            
            sell = sell + 1

        return maxP


