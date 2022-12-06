""""
Submission Result: Time Limit Exceeded 
Last executed input:
7168
"""

class Solution:
    def numSquares(self, n: int) -> int:
        maxroot = int(n ** 0.5)
        factors = [i*i for i in range(1, maxroot+1, 1)]
        
        # addition elements count list
        conbines = []
        for i in range(len(factors)):
            conbine = [0] * len(factors)
            conbine[i] += 1
            conbines.append(conbine)
            
        # print(conbines)  
        q = deque(zip(factors, conbines))
        # print(list(q))
        # for check seen 
        bags = defaultdict(set)        
        res =1
                     
        while q:
            size = len(q)
            for _ in range(size):
                
                curr, conbine = q.popleft()
                # print((curr, conbine))
                if curr == n:
                    return res                
                bags[conbine[0]].add(tuple(conbine))
                
                for i, f in enumerate(factors):
                    curr += f
                    if curr > n:
                        curr -= f
                        continue
                    
                    conbine[i] += 1   
                    if tuple(conbine) in bags[conbine[0]]:
                        # restore origin curr, conbine
                        curr -= f
                        conbine[i] -=1
                        continue
                    
                    q.append((curr, conbine))
                    curr -=f
                    conbine[i] -= 1            
            res += 1            
        return n
        
        
        