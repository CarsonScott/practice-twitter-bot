import tweepy

api_key = 't9eARRLZC6fMjKFiJTLKS3Xhu'
api_secret_key = 'DKIZJIFaQA8B4vlQmIg7EqlnTY8W7mPcK0FMMbpvmYh9Q8NBDu'
access_token = '1069410435458392064-UPVZQExrcnMLNERU6gmnV7Nr2lIIKz'
access_secret_token = 'xabrypzJRUrsHBIRzQvD2E1lTaHhOLgMnOIw6qYwuyrEc'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)

tweets=api.home_timeline(count=50)
for tweet in tweets:
	tweet.favorite()

