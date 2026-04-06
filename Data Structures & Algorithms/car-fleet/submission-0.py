class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time, stack = [], []
        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            time.append((position[i], t))
        time.sort(key=lambda x: x[0])
        for i, (p, t) in enumerate(time):
            while stack and stack[-1][1] <= t:
                stack.pop()
            stack.append((p, t))
        return len(stack)