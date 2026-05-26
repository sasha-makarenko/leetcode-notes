class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        postfix = [1] * len(nums)
        for j in range(len(nums)-2,-1,-1):
            postfix[j] = postfix[j+1] * nums[j+1]

        result = []
        for i in range(len(prefix)):
            result.append(prefix[i] * postfix[i])
        return result