class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        p = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    k = prices[i]-prices[j]
                    p.append(k)
                    break
                else:
                    if j == len(prices) - 1:
                        p.append(prices[i])
        p.append(prices[-1])
        print(p)
        return p