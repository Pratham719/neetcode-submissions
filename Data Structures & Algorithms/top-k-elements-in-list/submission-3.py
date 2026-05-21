class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        r = []
        for key in nums:
            f[key] = f.get(key, 0) + 1

        sor = sorted(f.items(), key=lambda x: x[1], reverse=True)

        for i in sor[:k]:
            r.append(i[0])
        return r
            
