class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_num = {}
        for index, value in enumerate(nums):
            if target-value in required_num:
                return [min(index, required_num[target-value]), max(index, required_num[target-value])]
            else:
                required_num[value] = index