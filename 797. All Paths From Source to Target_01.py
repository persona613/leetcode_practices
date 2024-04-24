"""
Wrong Answer
1 / 30 testcases passed

Input
graph =
[[1,2],[3],[3],[]]

Use Testcase
Output
[[0,1,3,3],[0,2,3,3]]
Expected
[[0,1,3],[0,2,3]]
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def backtrack(i, path):
            if i == len(graph) - 1:
                ans.append(path[:])
                return

            for node in graph[i]:
                path.append(node)
                backtrack(i + 1, path)
                path.pop()

        ans = []
        backtrack(0, [0])
        return ans