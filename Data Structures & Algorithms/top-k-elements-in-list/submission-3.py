class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_nums = []
        hashMap = {}
        for i in nums:
            if i in hashMap.keys():
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        sorted_nums = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            frequent_nums.append(sorted_nums[i][0])

        return frequent_nums

