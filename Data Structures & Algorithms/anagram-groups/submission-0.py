class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_arr = []
        hashMap = {}
        for i in strs:
            sort =  ''.join(sorted(i))
            if sort in hashMap.keys():
                hashMap[sort].append(i)
            else:
                hashMap[sort] = [i]
        for m in hashMap:
            anagram_arr.append(hashMap[m])
        return anagram_arr
        