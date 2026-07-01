class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int) 
        maxf=0
        i=0
        for j in range(len(s)):
            count[s[j]]+=1
            maxf=max(maxf,count[s[j]])
            if (j-i+1)-maxf>k:
                count[s[i]]-=1
                i+=1
        return j-i+1
