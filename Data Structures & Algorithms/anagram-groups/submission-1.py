class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for s in strs:
            sortedWord = "".join(sorted(s))
            if sortedWord in hashmap:
                hashmap[sortedWord].append(s)
                print(sortedWord)
            else:
                hashmap[sortedWord] = [s]
        for key,v in hashmap.items():
            res.append(v)
        
        return res
  
        
        