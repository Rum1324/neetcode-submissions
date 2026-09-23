class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        current_max = 0
        counter = min(1, len(nums))
        print(nums)
        i = 1
        while i < len(nums):
            if nums[i]-1 == nums[i-1]:
                counter += 1
            else:
                current_max = max(current_max, counter)
                counter = 1
            i += 1
        
        current_max =  max(current_max, counter)
        return current_max
