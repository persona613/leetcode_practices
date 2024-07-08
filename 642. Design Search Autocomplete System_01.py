"""
Wrong Answer
2 / 43 testcases passed
submitted at Apr 30, 2024 18:52

Editorial
Input
["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input"]
[[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"]]

Output
[null,["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[],["i a","i love you","island"],["i a","i love you","i love leetcode"],["i a"],[],["i a","i love you","island"],["i a","i love you","i love leetcode"],["i a"],[]]
Expected
[null,["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[],["i love you","island","i love leetcode"],["i love you","i love leetcode","i a"],["i a"],[],["i love you","island","i a"],["i love you","i a","i love leetcode"],["i a"],[]]
"""
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.marktime = "Time"
        self.trie = self.Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])
        
        self.curr_time = max(times)
        self.type_in = []
        self.curr = self.trie.root # level down with type_in

    def input(self, c: str) -> List[str]:
        self.curr_time += 1
        if c == "#":
            self.trie.insert("".join(self.type_in), self.curr_time)
            self.type_in = []
            self.curr = self.trie.root
            return []
        else:
            self.type_in.append(c)
            # curr_node level down
            self.curr = self.curr.setdefault(c, dict())

            q = self.dfs_search(self.curr, [], self.type_in)
            print(q)
            # sort q for return
            tmp = []
            while q:
                mktime, sen = q.pop()
                heapq.heappush(tmp, (-mktime, sen))
            while tmp:
                q.append(heapq.heappop(tmp)[1])
            return q[:3]

    # node = curr_trie_node, q = min heap, bag = collect string
    def dfs_search(self, node, q, bag):
        if self.marktime in node:
            if len(q) < 3 or node[self.marktime] >= q[0][0]:
                sen = "".join(bag)
                heapq.heappush(q, (node[self.marktime], sen))

        for key in node:
            if key == self.marktime:
                continue
            bag.append(key)
            next_node = node.setdefault(key, dict())
            self.dfs_search(next_node, q, bag)
            # backtrack
            bag.pop()
        return q

    # inner class
    class Trie:
        def __init__(self):
            self.root = dict()
            self.marktime = "Time"

        def insert(self, word, time):
            curr = self.root
            for c in word:
                curr = curr.setdefault(c, dict())
            # mark type in time
            curr[self.marktime] = time



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)