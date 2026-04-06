import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.post_id = 0
        self.follow_list = defaultdict(set)
        self.posts = []  # [-post_id, userId, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, [-self.post_id, userId, tweetId])
        self.post_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets, popped_tweets = [], []
        while len(tweets) < 10 and self.posts:
            post_id, user_id, tweet_id = heapq.heappop(self.posts)
            popped_tweets.append([post_id, user_id, tweet_id])
            if user_id == userId or user_id in self.follow_list[userId]:
                tweets.append(tweet_id)
        for t in popped_tweets:
            heapq.heappush(self.posts, t)
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_list[followerId]:
            self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_list[followerId]:
            self.follow_list[followerId].remove(followeeId)