class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        dp = {}
        dp[0] = [1]

        def search(target):
            if target < 0:
                return 0
            if target in dp:
                return dp[target]
            comb_sum = 0
            for num in nums:
                if target > num:
                    comb_sum += search(target - num)
                elif target == num:
                    comb_sum += 1
            dp[target] = comb_sum
            return comb_sum

        return search(target)

a = Solution()
print(a.combinationSum4([1, 2, 3], 4))