from collections import defaultdict
from heapq import heapify, heappop, heappush

class Twitter:
    def __init__(self):
        self.total_posts = 0
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.total_posts, tweetId))
        self.total_posts -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_posts = [post for post in self.posts[userId]]
        for followee in self.follows[userId]:
            for post in self.posts[followee]:
                all_posts.append(post)

        heapify(all_posts)
        res = []
        while all_posts and len(res) < 10:
            res.append(heappop(all_posts)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
