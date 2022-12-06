'''
Runtime: 35 ms, faster than 86.55% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 71.59% of Python3 online submissions
'''

class Solution:
    def decodeString(self, s: str) -> str:
        def seperate(tmp):
            string = ""
            digit = ""
            for t in tmp:
                if t.isdigit():
                    digit += t
                else:
                    string += t
            return (string, digit)
        
        def decode(s):
            bak = []
            tmp = ""
            q = deque()
            ans = ""
            
            for ss in s:
                tmp += ss
                if ss == "[":
                    # first bracket, push out tmp
                    if not bak:
                        tmp = tmp[:-1]
                        if tmp.isdigit():
                            q.append(tmp)
                        else:
                            string, digit = seperate(tmp)
                            for i in ("1", string, digit): q.append(i)
                                
                        tmp = ""
                    bak.append(ss)
                elif ss == "]":
                    bak.pop()
                    # last bracket, decode tmp
                    if not bak:
                        tmp = tmp[:-1]
                        # print(tmp)
                        if "[" in tmp:
                            string = decode(tmp)
                            q.append(string)                                
                        else:
                            q.append(tmp)
                        tmp = ""
            if tmp:
                for i in ("1", tmp): q.append(i); tmp = ""
                        
            while q:
                d = q.popleft()
                st = q.popleft()
                ans += int(d)*st
            return ans
        
        return decode(s)
            
                    