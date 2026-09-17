class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # okay so get the max of piles, thats the max u eat per thing
        # start from one
        # do binary search condition based
        # run a while loop thru out simulation where you divide by current k for hours taken, subtracting from total

        left = 1
        right = max(piles)

        while left < right:
            middle = left + ((right - left ) // 2)
            if self.evaluate_speed(piles,h, middle):
                right = middle
            else:
                left = middle + 1
        return left

    
    def evaluate_speed(self, piles, h, k):
        hours = 0

        for pile in piles:
            hours += ceil(pile / k)
            if hours > h:
                return False
        
        return True

        