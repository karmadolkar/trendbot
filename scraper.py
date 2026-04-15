import requests
import snscrape.modules.twitter as sntwitter

def reddit_trends():

    url = "https://www.reddit.com/r/startups/top.json?limit=10"
    headers = {"User-Agent": "trendbot"}

    res = requests.get(url, headers=headers).json()

    posts = []

    for p in res["data"]["children"]:
        posts.append({
            "platform": "Reddit",
            "text": p["data"]["title"]
        })

    return posts


def twitter_trends():

    tweets = []

    for tweet in sntwitter.TwitterSearchScraper("AI startup").get_items():

        tweets.append({
            "platform": "Twitter",
            "text": tweet.content
        })

        if len(tweets) >= 10:
            break

    return tweets


def get_trends():

    trends = []
    trends += reddit_trends()
    trends += twitter_trends()

    return trends