class Twitter:

    def __init__(self):
        self.follower_dict = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        # followed tweets
        for followee in self.follower_dict[userId]:
            for time, tweet in self.tweets[followee]:
                heapq.heappush(news_feed, (time, tweet))

        # our tweets
        for time, tweet in self.tweets[userId]:
            heapq.heappush(news_feed, (time, tweet))

        ret = []
        for _ in range(10):
            if news_feed:
                time, tweet = heapq.heappop(news_feed)
                ret.append(tweet)
            else:
                break

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follower_dict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_dict[followerId]:
            self.follower_dict[followerId].discard(followeeId)
