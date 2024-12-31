"""
149 ms runtime beats 77.47%
32.54 MB memory beats 36.69%
"""
class AllOne:

    def __init__(self):
        self.word_cnt = defaultdict(int)
        # double-link-list
        self.dummy = Dnode(0, "#")
        self.cnt_node = {0: self.dummy}
        self.tail = self.dummy

    def inc(self, key: str) -> None:
        self.word_cnt[key] = self.word_cnt.get(key, 0) + 1
        self.inc_update(key)

    def dec(self, key: str) -> None:
        self.word_cnt[key] -= 1
        self.dec_update(key)

    def getMaxKey(self) -> str:
        if self.tail == self.dummy:
            return ""
        for e in self.tail.words:
            return e

    def getMinKey(self) -> str:
        if not self.dummy.next:
            return ""
        for e in self.dummy.next.words:
            return e

    def inc_update(self, key):
        insert_curr_node = False
        delete_pre_node = False

        curr_cnt = self.word_cnt[key]
        # pre_cnt and pre_node must exist
        pre_cnt = curr_cnt - 1
        pre_node = self.cnt_node[pre_cnt]

        # update dict:cnt_node
        if pre_cnt > 0:
            pre_node.words.remove(key)
        if not pre_node.words:
            del self.cnt_node[pre_cnt]
            delete_pre_node = True

        if curr_cnt not in self.cnt_node:
            curr_node = Dnode(curr_cnt, key)
            self.cnt_node[curr_cnt] = curr_node
            insert_curr_node = True
        else:
            curr_node = self.cnt_node[curr_cnt]
            curr_node.words.add(key)

        # update DLL
        if insert_curr_node and delete_pre_node:
            self.replace_node(pre_node, curr_node)
        elif insert_curr_node:
            self.insert_node(pre_node, curr_node)
        elif delete_pre_node:
            self.delete_node(pre_node)

    def dec_update(self, key):
        insert_curr_node = False
        delete_nxt_node = False

        curr_cnt = self.word_cnt[key]
        # nxt_cnt and nxt_node must exist
        nxt_cnt = curr_cnt + 1
        nxt_node = self.cnt_node[nxt_cnt]
        
        # update dict:cnt_node
        nxt_node.words.remove(key)
        if not nxt_node.words:
            del self.cnt_node[nxt_cnt]
            delete_nxt_node = True

        if curr_cnt not in self.cnt_node:
            curr_node = Dnode(curr_cnt, key)
            self.cnt_node[curr_cnt] = curr_node
            insert_curr_node = True
        else:
            curr_node = self.cnt_node[curr_cnt]
            if curr_cnt > 0:
                curr_node.words.add(key)

        # update DLL
        if insert_curr_node and delete_nxt_node:
            self.replace_node(nxt_node, curr_node)
        elif insert_curr_node:
            # insert before nxt_node from left
            self.insert_node(nxt_node.pre, curr_node)
        elif delete_nxt_node:
            self.delete_node(nxt_node)

    def replace_node(self, old_node, new_node):
        old_node.pre.next = new_node
        new_node.pre = old_node.pre
        if old_node.next:
            new_node.next = old_node.next
            old_node.next.pre = new_node
        if self.tail == old_node:
            self.tail = new_node
    
    def insert_node(self, pre_node, curr_node):
        tmp_node = pre_node.next
        pre_node.next = curr_node
        curr_node.pre = pre_node
        if tmp_node:
            curr_node.next = tmp_node
            tmp_node.pre = curr_node
        if self.tail == pre_node:
            self.tail = curr_node

    def delete_node(self, target_node):
        if target_node.next is None:
            target_node.pre.next = None
            if self.tail == target_node:
                self.tail = target_node.pre
        else:
            target_node.pre.next = target_node.next
            target_node.next.pre = target_node.pre


class Dnode:
    def __init__(self, val, word):
        # val = count
        self.val = val
        self.words = {word}
        self.pre = None
        self.next = None

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()