from collections import deque
class RecentCounter:

    def __init__(self):
        self.dp=deque()

    def ping(self, t: int) -> int:

        while self.dp and self.dp[0] < t-3000:
            self.dp.popleft()
        
        self.dp.append(t)

        return len(self.dp)
    

counter = RecentCounter()
print(counter.ping(1))    
print(counter.ping(100))  
print(counter.ping(3001)) 
print(counter.ping(3002))
print(counter.ping(3003))
