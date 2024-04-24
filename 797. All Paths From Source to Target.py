"""
87 ms runtime beats 6.41%
18.30 MB memory beats 46.71%
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def backtrack(i, path):
            if i == len(graph) - 1:
                ans.append(path[:])
                return

            for node in graph[i]:
                path.append(node)
                backtrack(node, path)
                path.pop()

        ans = []
        backtrack(0, [0])
        return ans