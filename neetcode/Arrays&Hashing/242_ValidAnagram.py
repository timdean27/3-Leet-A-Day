# Given tow strings s and t , return true if t is an anagram of s , and false otherswise.

class Solution():
    def isAnagram(self,s: str ,t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(t) != len(s):
            return False
        # make empy hashes
        countS , countT = {} ,{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            # find key of letter i in s , if key does not exist 
            # .get will set a deffulat value of 0 to the key and we add 1
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
    
sol = Solution()
ans = sol.isAnagram("anagram" , "nagaram")
print(ans)