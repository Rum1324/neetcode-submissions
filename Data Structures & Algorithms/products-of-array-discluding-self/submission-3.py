class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [x * nums[i] for i, x in enumerate([0] + nums)]
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # nums=[1,2,4,6]

        """
        prefix = [1,1,1,1]
        suffix = [1,1,1,1]

        prefix = [1,1,2,8]
        suffix = [48,24,6,1]
        """

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            
            i = -i-1
            suffix[i] = suffix[i+1] * nums[i+1]
        
        
        return [prefix[i] * suffix[i] for i in range(len(nums))]