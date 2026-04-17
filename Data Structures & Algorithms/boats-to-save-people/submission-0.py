class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 5, 1, 4, 2    limit = 6
        # boat able to carry at most 2 people
        # 1, 2, 4, 5
        # 1, 2, 2, 3, 3  limit = 3
        people.sort()
        boats = 0
        l, r = 0, len(people) - 1
        while l < r:
            if people[l] + people[r] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1
            
            boats += 1

        if r == l:
            boats += 1
            
        return boats