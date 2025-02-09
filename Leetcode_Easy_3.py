class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n=len(s)
        res=0
        for i in range(n):
            if i+1<n and roman[s[i]]<roman[s[i+1]]:
                res-=roman[s[i]]
            else:
                res+=roman[s[i]]
        return res