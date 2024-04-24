"""
29 ms runtime beats 93.17%
16.50 MB memory beats 67.96%
"""
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not bank: return -1
        if endGene not in bank:
            return -1
        
        def mutate(gene):
            for i in range(len(gene)):
                curr = gene[i]
                for mu in gpool:
                    if mu != curr:
                        yield gene[:i] + mu + gene[i+1:]

        gpool = "ACGT"
        bk = set(bank)
        q = deque([(startGene, 0)])
        while q:
            curr, p = q.popleft()
            if curr == endGene:
                return p
            gen = mutate(curr)
            while True:
                nxt = next(gen, None)
                if not nxt:
                    break
                if nxt in bk:
                    bk.remove(nxt)
                    q.append((nxt, p + 1))
        return -1
