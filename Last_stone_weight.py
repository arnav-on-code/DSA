#LC- 1046

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones=[-x for x in stones]
        heapq.heapify(stones)

        while len(stones) >1:
            y= -heapq.heappop(stones)
            x= -heapq.heappop(stones)

            if y!=x:
                heapq.heappush(stone, -(y-x))
        
        if stones:
            return -stones[0]
        return 0