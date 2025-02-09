class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_val=""
        for i in range(len(strs[0])):
            for s in strs:  #floor, len(floor)-> 5
                if i+1>len(s) or s[i]!=strs[0][i]:
                    return strs_val
            strs_val+=strs[0][i]
        return strs_val
                