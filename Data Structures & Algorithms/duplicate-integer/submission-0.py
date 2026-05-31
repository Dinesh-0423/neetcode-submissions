class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for index, i in enumerate(nums):
            if i in hashMap:
                return True
            hashMap[i] =index
        return False



        