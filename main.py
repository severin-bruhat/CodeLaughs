import tweepy
import firebase_admin
import random
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
import os
import requests

# Load environment variables from the .env file
load_dotenv('.env')

# Access Twitter API credentials
twitter_consumer_key = os.environ.get('TWITTER_API_KEY')
twitter_consumer_secret = os.environ.get('TWITTER_API_SECRET')
twitter_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# Initialise Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Authenticate with Twitter API
client = tweepy.Client(consumer_key=twitter_consumer_key,
                       consumer_secret=twitter_consumer_secret,
                       access_token=twitter_access_token,
                       access_token_secret=twitter_access_token_secret)

# array of hashtags
hashtags = [
    "#CodeLaughs",
    "#ProgrammingHumor",
    "#DevLife",
    "#TechHumor",
    "#CodeJokes",
    "#ProgrammerHumor",
    "#TechJokes",
    "#GeekHumor",
    "#NerdyLaughs",
    "#LaughAtCodeComment",
    "#TechLaughs",
    "#CodingComedy",
    "#LaughWhileCoding",
    "#CodeFunny",
    "#ProgrammerLaughs",
    "#TechFunnies"
]

# Function to get a random comment with null flag from Firestore


def get_random_comment():
    comments_ref = db.collection("comments")
    query = comments_ref.where("flag", "==", None).limit(1).stream()
    for doc in query:
        return {"id": doc.id, "content": doc.to_dict()}
    return None

# Function that generate an image with Carbon


def generate_image(text):
    api_url = "https://carbonara.solopov.dev/api/cook"

    headers = {
        'Content-Type': 'multipart/form-data',
    }

    parameters = {
        "code": text,
        "widthAdjustment": "false",
    }

    response = requests.post(api_url, files=parameters)

    if response.status_code == 200:
        try:
            image_path = 'tweet_image.png'
            with open(image_path, 'wb') as f:
                print(response.status_code)
                f.write(response.content)
            print("Image generated.")
            return image_path
        except Exception as e:
            print("Error occurred while generating the image:", e)
            return False

    return False


# Function to post a comment on Twitter and update the flag in Firestore

def post_comment(comment):
    tweet = comment["content"]["text"]
    tweet_id = comment["id"]
    try:
        random_hashtag = random.choice(hashtags)
        client.create_tweet(text=tweet + " " + random_hashtag)
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
