class Solution:
    from collections import Counter
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-k+1):
            l=nums[i:i+k]
            l1=Counter(l)
            l1=dict(sorted(l1.items(),reverse=True,key=lambda item:item[1]))
            d = defaultdict(list)
            res=[]
            for key, value in l1.items():
                d[value].append(key)

            for i in d.keys():
                d[i].sort(reverse=True)
                for j in d[i]:
                    if len(res)==x:
                        break
                    res.append(j)

            sum1=0
            for i in res:
                sum1+=(l1[i]*i)
            ans.append(sum1)

        return ans