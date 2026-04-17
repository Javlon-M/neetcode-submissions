class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1 + 3 = 4 + 3 = 7 + 3 = 10
        # 4 + 2 = 6 + 2 = 8 + 2 = 10

        # [(1,3), (4,2)]
        # [(4,2), (1,3)]
        # [3]
        # 
        # [(7, 1), (4, 3), (1, 2), (0, 1)]
        # [3, 4.5, 10]
        
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars = sorted(cars, key=lambda x:x[0], reverse=True)
        stack = []
        for (p, s) in cars:
            time = (target - p)/s

            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)
