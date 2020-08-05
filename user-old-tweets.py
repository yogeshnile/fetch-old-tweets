#author   :- Yogesh Nile
#Email    :- yogeshnile.work4u@gmail.com
#Twitter  :- twitter.com/YogeshNile
#GitHub   :- github.com/yogeshnile


import GetOldTweets3 as got   #https://pypi.org/project/GetOldTweets3/
import pandas as pd

user_name = "elonmusk"  #put twitter user id without @
start_date = "2016-01-01" #yy-mm-dd
end_date = "2016-12-31" #yy-mm-dd

tweetCriteria = got.manager.TweetCriteria().setUsername(user_name).setSince(start_date).setUntil(end_date)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)

tweet_text = []
tweet_id = []
tweet_link = []
tweet_urls = []

for t in tweet:
	linkd = "https://twitter.com/"+user_name+"/status/"+str(t.id)
	tweet_link.append(linkd)
	tweet_id.append(t.id)
	tweet_text.append(t.text)
	tweet_urls.append(t.urls)

list_of_tuples = list(zip(tweet_id, tweet_text, tweet_urls, tweet_link))
df = pd.DataFrame(list_of_tuples, columns = ['tweet-id', 'tweet-text', 'include-links', 'tweet-url'])

file_name = user_name+" "+start_date+" to "+end_date+" tweets.csv"
df.to_csv(file_name)
