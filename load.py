# load the comments into Firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to add a comment to Firestore
# array of comments
comments = [
    "This code is like a roller coaster ride. Buckle up and hold on tight!",
    "Bug defeated! The infinite loop that sent the program into a time warp has been terminated.",
    "Resolved the bug that turned the login button into a mischievous shape-shifter.",
    # Add more comments as needed
]


def add_comment(comment):
    comments_ref = db.collection("comments")
    comments_ref.add({
        "text": comment,
        "flag": None
    })


# Example usage
for comment in comments:
    add_comment("// " + comment)
    print(comment + "added")
