class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        indexarr = []
        for index, i in enumerate(nums):
            total = target - i
            if total in hashMap:
                indexarr.append(hashMap[total])
                indexarr.append(index)
                return indexarr
            hashMap[i] = index
        return indexarr

