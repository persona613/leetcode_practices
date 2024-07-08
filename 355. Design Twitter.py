"""
45 ms runtime beats 5.95%
16.64 MB memory beats 79.53%
"""
class Twitter:

    def __init__(self):
        # timecode
        self.counter = count()
        # {userId: {followees}}
        self.followees = defaultdict(set)
        # {userId: deque()}
        self.postboard = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        code = next(self.counter)
        self.postboard[userId].append((-code, tweetId))
        if len(self.postboard[userId]) > 10:
            self.postboard[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        followees = self.followees[userId].union({userId})
        for followee in followees:
            news += self.postboard[followee]
        heapq.heapify(news)
        res = []
        while news and len(res) < 10:
            code, tid = heapq.heappop(news)
            res.append(tid)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)