class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq: freq[n] += 1
            else: freq[n] = 1

        listnums = []
        for i in range(0, k):
            addin = max(freq, key=freq.get)
            listnums.append(addin)
            freq[addin] = 0

        return listnums