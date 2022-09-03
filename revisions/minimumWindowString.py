class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        countT, window = {},{}
        
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)

        have,need = 0, len(countT)

        res = ""
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
        
            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                window[s[l]] -= 1
                # its < because we could have more than needed
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                # recompute the res
                if r - l + 1 < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                l += 1

        return res


            
