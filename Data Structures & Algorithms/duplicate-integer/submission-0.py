class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        ans = []

        for num in nums:
            if num in ans:
                return True
            else:
                ans.append(num)
        return False
        