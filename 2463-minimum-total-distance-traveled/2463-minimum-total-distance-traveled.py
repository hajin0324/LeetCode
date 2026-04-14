class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        slots = []
        for pos, limit in factory:
            slots.extend([pos] * limit)

        R, F = len(robot), len(slots)
        INF = 10**20

        dp = [[INF] * (F + 1) for _ in range(R + 1)]
        
        for j in range(F + 1):
            dp[0][j] = 0  

        for i in range(1, R + 1):
            for j in range(1, F + 1):
                dp[i][j] = dp[i][j-1]

                if i <= j:
                    cost = abs(robot[i-1] - slots[j-1])
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + cost)

        return dp[R][F]