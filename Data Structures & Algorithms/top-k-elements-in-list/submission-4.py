class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        result = []
        for i in range(k):
            result.append(counter[i][0])
        return result