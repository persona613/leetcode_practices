"""
36 ms runtime beats 56.53%
16.70 MB memory beats 28.74%
"""
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dic = self.parse(formula, 1)
        atoms = sorted(dic.keys())
        res = []
        for atom in atoms:
            res.append(atom)
            if dic[atom] > 1:
                res.append(str(dic[atom]))
        return "".join(res)
    
    def parse(self, foma, factor):
        dic = defaultdict(int)
        name = []
        count = []
        i = 0
        n = len(foma)
        while i < n:
            curr = foma[i]
            if curr == "(":
                # add pre atom and list.clear()
                self.register(name, count, dic)

                # detect close bracket
                stk = 1
                i += 1
                start = i
                while stk:
                    if foma[i] == "(":
                        stk += 1
                    elif foma[i] == ")":
                        stk -= 1
                    i += 1
                end = i - 1

                # detect factor
                fac_start = i
                while i < n and foma[i].isdigit():
                    i += 1

                # parse to a dict
                if i == fac_start:
                    fac = 1
                else:
                    fac = int(foma[fac_start: i])
                ret = self.parse(foma[start: end], fac)

                # add to curr-dict
                for key in ret:
                    dic[key] += ret[key]
                continue
            else:
                if curr.isupper():
                    self.register(name, count, dic)
                    name.append(curr)
                elif curr.isalpha():
                    name.append(curr)
                else:
                    count.append(curr)
            i += 1

        self.register(name, count, dic)
        for key in dic:
            dic[key] *= factor
        return dic

    def register(self, name, count, dic):
        if not name:
            return
        cnt = int("".join(count)) if count else 1
        dic["".join(name)] += cnt
        name.clear()
        count.clear()