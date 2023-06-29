import tweepy
import firebase_admin
import random
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv('.env')

# Access Twitter API credentials
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


# Initialise Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Authenticate with Twitter API
client = tweepy.Client(consumer_key,
                       consumer_secret,
                       access_token,
                       access_token_secret)

# Function to get a random comment with null flag from Firestore


def get_random_comment():
    comments_ref = db.collection("comments")
    query = comments_ref.where("flag", "==", None).limit(1).stream()
    for doc in query:
        return {"id": doc.id, "content": doc.to_dict()}
    return None

# Function to post a comment on Twitter and update the flag in Firestore


def post_comment(comment):
    tweet = comment["content"]["text"]
    tweet_id = comment["id"]
    try:
        client.create_tweet(text=tweet + " #CodeLaughs #ProgrammerHumor")
        print("Comment posted on Twitter:", tweet)
    except tweepy.TweepError as e:
        print("Error occurred while posting the comment:", e)
        return False

    try:
        # Update the flag to true in Firestore
        comment_ref = db.collection("comments").document(tweet_id)
        comment_ref.update({"flag": True})
        print("Flag updated to True in Firestore.")
    except Exception as e:
        print("Error occurred while updating the flag in Firestore:", e)
        return False

    return True


# Get a random comment and post it on Twitter
random_comment = get_random_comment()

if random_comment:
    if not post_comment(random_comment):
        print("Failed to post the comment and update the flag.")
else:
    print("No comments with null or false flag found in Firestore.")
