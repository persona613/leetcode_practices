"""
1035 ms runtime beats 5.15%
51.48 MB memory beats 6.23%
"""
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # calculate subtrees' size at fix root
        def dfs_size(node, parent):
            cnt = 1
            for child in gf[node]:
                if child != parent:
                    cnt += dfs_size(child, node)
            size[node] = cnt
            return cnt

        # calculate subtrees' size at dynamic root
        def dfs_dpsize(root, pre_root):
            x, y = size[root], size[pre_root]
            # subsize transfer to curr-root
            size[root], size[pre_root] = n, n - x

            for child in gf[root]:
                memo[(child, root)] = size[child]
                if child != pre_root:
                    dfs_dpsize(child, root)
            # restore size array for dfs
            size[root], size[pre_root] = x, y

        gf = defaultdict(set)
        for u, v in edges:
            gf[u].add(v)
            gf[v].add(u)
        
        # calculate all subtrees' size at root-0
        size = [0] * n
        dfs_size(0, None)
        # calculate subtrees' size at every root
        # memo={(subtree, root): subtree's size}
        memo = dict()
        dfs_dpsize(0, 0)

        # calcualte pathsum(0)
        cnt0 = 0
        q = deque([(0, 0, None)]) # (node, path_count, parent)
        while q:
            curr, pcnt, parent = q.popleft()
            cnt0 += pcnt
            for child in gf[curr]:
                if child != parent:
                    q.append((child, pcnt + 1, curr))

        # sum(j) = sum(i) - count(j,i) + count(i,j)
        res = [None] * n
        res[0] = cnt0
        q = deque([0])
        while q:
            curr = q.popleft()
            for adj in gf[curr]:
                if res[adj] == None:
                    res[adj] = res[curr] - memo[(adj, curr)] \
                                + memo[(curr, adj)]
                    q.append(adj)
        return res      