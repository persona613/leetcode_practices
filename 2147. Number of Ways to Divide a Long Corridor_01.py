"""
Wrong Answer
111 / 248 testcases passed
Editorial
Input
corridor =
"PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"

Use Testcase
Output
1920000000
Expected
919999993
"""        
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # seat index
        sd = []
        for i in range(len(corridor)):
            if corridor[i] == "S":
                sd.append(i)
        sm = len(sd)
        if sm < 2 or sm % 2 == 1:
            return 0
        ans = 1
        for i in range(1, len(sd)-1, 2):
            ans *= sd[i+1] - sd[i]
        return ans