from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i]+=1
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for num,count in freq.items():
            buckets[count].append(num)
        results=[]
        for count in range(n,0,-1):
            for n in buckets[count]:
                results.append(n)
                if len(results)==k:
                    return results
        return results