import snscrape.modules.twitter as sntwitter
import csv
maxTweets =10000

csvFile = open('38.csv', 'a', newline='', encoding='utf8')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['username'])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('TAT').get_items()):
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.user.username])
        print(tweet.user.username)
csvFile.close()

