# Presentation

This bot post messages into a Tweeter account.
Those messages come from a Firestore document database:

```
{
    id: autoGeneratedId,
    text: message,
    flag: null|True
}
```

Once sent, the flag is set to True so we don't re-send it.

# Dependencies

## Dotenv

Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.

`pip3 install python-dotenv`

Copy the `.env.dist` file and rename it `.env` use it to store your Twitter auth details.

## Firebase (Firestore)

We use Firestore to store the comments as documents.

`pip3 install firebase_admin`

You will nee to create a `serviceAccountKey.json` file.

To obtain the serviceAccountKey.json file for Firebase, follow these steps:

- Go to the Firebase Console (https://console.firebase.google.com/) and open your project.

- Click on the gear icon next to "Project Overview" and select "Project settings".

- In the "Service Accounts" tab, scroll down to the "Firebase Admin SDK" section.

- Click on the "Generate new private key" button. This will download the serviceAccountKey.json file to your computer.

- Save the downloaded serviceAccountKey.json file in a secure location on your machine.

## Tweepy

Tweepy is the library we use to interact with the Twitter API.

`pip3 install tweepy`

Official documentation: https://docs.tweepy.org/en/stable/client.html

# Usage

## Load the messages into Firestore

Edit `load.py` and add your messages into the `comments` array.
The run `python3 load.py`

## Post a message

Run `python3 main.py`
You can schedule a cronjob to run this command on a regular basis.
