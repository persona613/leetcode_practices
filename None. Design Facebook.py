"""
185 ms runtime beats None %
17.8 MB memory beats None %
"""
class Facebook:

    def __init__(self):
        self.friends = defaultdict(set)
        self.posts = []

    def writePost(self, userId: int, postContent: str) -> None:
        self.posts.append((userId, postContent))

    def addFriend(self, user1: int, user2: int) -> None:
        self.friends[user1].add(user2)
        self.friends[user2].add(user1)

    def showPosts(self, userId: int) -> List[str]:
        res = []
        fds = self.friends[userId]
        for po in self.posts[::-1]:
            if po[0] in fds:
                res.append(po[1])
        return res


# Your Facebook object will be instantiated and called as such:
# obj = Facebook()
# obj.writePost(userId,postContent)
# obj.addFriend(user1,user2)
# param_3 = obj.showPosts(userId)