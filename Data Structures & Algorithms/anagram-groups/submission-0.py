class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result= defaultdict(list) #make mpty dict whnvr new key comes autmticly create empty list for that key=> {} empty but with special behaviour
        for w in strs: #iterate on each word
            sortedWords = ''.join(sorted(w)) #sorted() returns a list of characters so need join, strings are immutable so no sort()
            result[sortedWords].append(w) # res[key]->append(value)
        return list(result.values()) #values() method of dict return values and typecasted to list
            

