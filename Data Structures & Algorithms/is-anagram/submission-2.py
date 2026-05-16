class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check lenght
        if len(s)!=len(t):
            return False
        #empty hmap/dict
        hmapS , hmapT = {}, {}
        for i in range(len(s)):
        #iterate on both -> check count in dict -> update -> return check 
            hmapS[s[i]] = 1 + hmapS.get(s[i], 0)
            hmapT[t[i]] = 1 + hmapT.get(t[i], 0)
        return hmapS == hmapT
