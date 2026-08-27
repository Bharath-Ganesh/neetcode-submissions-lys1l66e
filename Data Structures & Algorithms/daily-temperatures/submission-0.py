class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n   = len(temperatures)
        res = [0] * n
        day_stack = []
        idx = 0
        while idx < n:
            temp = temperatures[idx]
            while day_stack and temperatures[day_stack[-1]] < temp:
                prev_idx = day_stack.pop()
                days = idx - prev_idx
                res[prev_idx] = days # [1,1, 1]

            day_stack.append(idx) # [1, 3, 4,]
            idx += 1
        return res
