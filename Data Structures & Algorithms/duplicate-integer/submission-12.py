class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                pass
            else:
                seen.add(x)
        if len (nums) == len (seen):
            return False
        else:
            return True