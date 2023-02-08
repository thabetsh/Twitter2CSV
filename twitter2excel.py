# import GetOldTweets3
#
# max_tweets = 10
#
# tweetCriteria = GetOldTweets3.manager.TweetCriteria().setUntil("2021-08-09").setQuerySearch("#وزارة_التعليم").setMaxTweets(max_tweets)
#
# for i in range(max_tweets):
#     tweet = GetOldTweets3.manager.TweetManager.getTweets(tweetCriteria)[i]
#     print(tweet.id)
#     print(tweet.username)
#     print(tweet.text)
#     print(tweet.date)

import snscrape.modules.twitter as sntwitter
import csv
maxTweets = 40000

#keyword = 'deprem'
#place = '5e02a0f0d91c76d2' #This geo_place string corresponds to İstanbul, Turkey on twitter.
#saudi 08b2d74428e2ca88
#keyword = 'covid'
#place = '01fbe706f872cb32' This geo_place string corresponds to Washington DC on twitter.

#Open/create a file to append data to
csvFile = open('result27.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['tweet','username','date','verified','followersCount','location'])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#وزارة_التعليم+since:2021-8-9 until:2022-4-4 -filter:links').get_items()):
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.content,tweet.user.username, tweet.date,  tweet.user.verified,tweet.user.followersCount,tweet.user.location])
csvFile.close()