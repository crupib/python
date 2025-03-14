class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        else:
            max_profit = 0
            min_price = prices[0]
            for i in range(len(prices)):
                profit = prices[i] - min_price
                max_profit = max(profit, max_profit)
                min_price = min(min_price, prices[i])

            return max_profit
def main():
   prices = [7, 1, 5, 3, 6, 4]
   sol = Solution()
   print(sol.maxProfit(prices))

if __name__ == "__main__":
    main()
