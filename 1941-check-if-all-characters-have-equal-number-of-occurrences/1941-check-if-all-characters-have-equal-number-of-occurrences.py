class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        li=[]
        for value in d.values():
            li.append(value)
        return len(set(li))==1
        