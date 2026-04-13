class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        plus = start
        minus = start
        cnt = 0

        if nums[start] == target:
            return 0

        for i in range(len(nums)):
            cnt += 1

            if plus < len(nums) - 1:
                plus += 1

            if minus != 0:
                minus -= 1

            if nums[plus] == target or nums[minus] == target:
                return cnt



# Input: nums, target, start

# nums[i] == target 일 때,
# abs(i - start)가 최소인 i

# start index에서 시작하고,
# start에서 양방향 (-, +)로 각 pointer 이동