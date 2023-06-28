import tweepy

try:

    client = tweepy.Client(consumer_key='5JvLVOrU8WUY4vYSCExyoa3Y9',
                           consumer_secret='1m1LlHEzINkD4seDdKOav2qYtEeHOM53nl3eDU8DRlijC9ksVm',
                           access_token='1673418124987625483-7cFBgLamMn2B95pYQxAxEEDdjC6m5X',
                           access_token_secret='I8ZBcJxLzRCSpgBNhLOOn6jDC6di7RBgCd3gH7oez64l4')

    response = client.create_tweet(text='hello world')
    print(response)

except tweepy.TweepError as e:
    print(e.message)
