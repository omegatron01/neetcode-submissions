class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        done = []
        for x in nums:
            if x in seen:
                pass
            else:
                seen.add(x)
                done.append(x)
        if len (nums) == len (seen):
            return False
        else:
            return True