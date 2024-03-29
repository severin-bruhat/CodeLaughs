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
    "Apologies for the spaghetti code, I was quite hungry while coding this.",
    "Beware all ye who enter! Here be dragons in the form of legacy code.", 
    "I learned programming from a cat, so don't judge me if this code is a little hairy.",
    "This module contains more hacks than a horror movie marathon.",
    "Hope you like puzzles, because understanding this code ain't easy.",
    "Who needs comments when you can decode my brilliant variable names instead?",
    "The ghost of coding past insists this be left as-is. *rattling chains*",
    "I got 99 problems but spaghetti code ain't one.",
    "This code was translated from Wingdings using Google Translate so good luck.",
    "Behold my signature one-liner functions! *drops mic*",
    "This module was created at 3am on a Saturday, please lower your expectations accordingly.",
    "We apologize for the mess. The intern who wrote this code promises to clean it up later.", 
    "I learned programming from reading IKEA instructions - so good luck assembling this code.",
    "This code has been passed down for generations - I dare not refactor the ancient incantations.",
    "Behold, my magnum opus! It may not be pretty, but it gets the job done. *hopefully*",  
    "The person who wrote this code clearly has a vendetta against future code maintainers.",
    "I consulted a Magic 8 ball on how to best implement this. Don't judge me.",
    "This was translated from Code Sans using Google Translate. Pardon the odd syntax.",
    "To understand this code, one must open their heart...and the nearest bottle of wine.",
    "Here be messy scripts written at 2am. Abandon all hope ye who read this.",
    "I was told to comment my code, but nobody said the comments had to make sense.",
    "This code works so beautifully I could cry. Please don't touch it.",
    "The bugs in this code were carefully cultivated over many late nights.",
    "I apologize if this code makes you scream. At least it's not a nightmare!",
    "This code may be quite messy, but at least it isn't haunted...I hope.",
    "These functions were created during a brief stint moonlighting as a magician.",
    "This module was translated from gibberish using an experimental AI translator.",
    "I wrote this code passive-aggressively after an argument with product managers.",
    "I consulted a fortune cookie to guide how this module should work. So far so good!",  
    "This code was written by my cat walking across the keyboard. Meow!",
    "I wrote this while listening to heavy metal music. So get ready to rock out!",
    "This code may be quite scary, but at least it keeps the bugs away!",
    "I wrote this code while binge watching Mad Men. It may get a bit dramatic at times.",
    "I apologize if this module causes confusion or tears. I was quite emotional while coding it.",
    "This code was written after drinking 3 cups of coffee and a Red Bull. Buckle up!",
    "I asked my 8 year old niece how I should implement this feature. Sorry in advance!",
    "This code was translated from emoji language. It may seem silly but somehow works!",
    "I wrote this while watching Stranger Things on Netflix. Things are about to get strange!",
    "I wrote this code passive-aggressively after an argument with product managers.",
    "This code may appear quite messy, but beauty is in the eye of the beholder!",
    "I wrote this code listening to soothing meditation music. Namaste!",
    "I wrote this code under the influence of chocolate and candy. Sugar rush coding!",
    "This code may act a bit weird. It was written under the influence of catnip tea.",  
    "I wrote this code while binge watching The Office. It may get a bit silly or awkward at times!",
    "I wrote this after eating spicy food for lunch. Apologies if the code burns your eyes!",
    "I wrote this code while listening to heavy metal music. So get ready to rock out!",  
    "This code was written while I was on the elliptical at the gym. Sweaty coding!",
    "I wrote this code passive-aggressively after an argument with designers.",
    "I asked my cat to write this code while I took a nap. Meow!",
    "I wrote this code while eating tacos for lunch. It may get a bit messy!",
    "I wrote this code after drinking 3 espresso shots in a row. Buckle up!",
    "I apologize in advance for this code - blame it on Monday morning and too much coffee.",
    "When I wrote this, only God and I understood what I was doing. Now, only God knows.",
    "I dedicate this bug to all the lost hours of debugging. May they rest in peace.",
    "This code block is like Schrödinger's cat. Don't look at it, or you might kill it!",
    "To understand recursion, you must first understand recursion.",
    "This function has more branches than my family tree.",
    "I'm not a magician, but I've got a few tricks up my sleeve. Behold, the disappearing bug!",
    "This code is as optimized as my morning routine. It's not.",
    "In case of fire: git commit, git push, then leave building.",
    "I have mixed tabs and spaces. May the coding gods have mercy on my soul.",
    "Here be dragons... and by dragons, I mean pointer arithmetic.",
    "This code is like an onion. It might make you cry.",
    "I wrote this under the influence... of tight deadlines.",
    "My grand plan is to replace this with something elegant. That was three years ago.",
    "If this works, it's not by accident.",
    "I came, I saw, I coded... and then I had to debug.",
    "This code is like a box of chocolates. You never know what you're gonna get.",
    "I'm not saying I hate this code, but I would unplug its life support to charge my phone.",
    "This is where I'd put a witty comment... IF I HAD ONE!",
    "Code so clean you can eat off it. Just kidding, please don't.",
    "If at first you don't succeed; call it version 1.0.",
    "This is my circus and these are my monkeys. Welcome to the function.",
    "Code so good, it makes your ex regret leaving you.",
    "Every time you use 'goto', a kitten cries in the programming world.",
    "Ssshhh... the variables are sleeping. Use 'const' to not wake them up.",
    "Some things are better left uncommented.",
    "This code is like a good joke - the beauty is in the execution.",
    "This code is a sandwich, unfortunately, it's mostly bread. #ToDo: Add the filling.",
    "It's not a bug – it's an undocumented feature.",
    "I tried to make this code idiot-proof, but they keep making better idiots.",
    "This is the code that made the Kessel Run in less than twelve parsecs.",
    "I must confess, this code was written by my cat walking on the keyboard.",
    "I'm not responsible for this code. They made me write it, against my will.",
    "Remember to always code as if the person who ends up maintaining your code is a violent psychopath who knows where you live.",
    "This code has been stress-tested. It stressed me a lot.",
    "I can explain it to you, but I can't understand it for you.",
    "This code is like a workout. You might not like it, but you know it's good for you.",
    "May the force be with you... You'll need it to understand this code.",
    "This code is cleaner than my room.",
    "The best part of this code is that by the time you've read this comment, it's already outdated.",
    "Who said coding isn't an extreme sport? This function is hanging by a thread!",
    "This code is like a fine wine. It needs to sit and mature.",
    "If you find this code readable, you might be a cyborg.",
    "Don't judge me for this code. It was a different time, I was a different developer.",
    "This code isn't slow, it's leisurely.",
    "This code is like a teenager - it doesn't clean up after itself.",
    "You can't handle the true power of this spaghetti code.",
    "This code is like a good friend - dependable, but sometimes a little messy.",
    "There's light at the end of the tunnel. I just hope it's not a train coming the other way.",
    "This code is my horcrux. Good luck destroying it.",
    "This code has as many issues as a soap opera character.",
    "I swear this code wasn't written by me, but by a very small rubber duck.",
    "This code runs on the power of hope and a couple of energy drinks.",
    "The person who can simplify this code has not been born yet.",
    "This code is like a group project. Everyone has touched it, but no one wants to claim it.",
    "I'm not saying this code is ugly, but it could use a bit of makeup.",
    "This code doesn't follow the principle of least astonishment. Brace yourself!",
    "This code is similar to my love life: full of exceptions.",
    "I reached the root of all evil and planted this code there.",
    "If this code worked first try, I'd be just as surprised as you.",
    "This code is its own documentation. Good luck!",
    "I'd tell you a joke about this code, but I'm afraid I'd have to debug the punchline.",
    "This loop has seen more iterations than my attempts at a healthy diet.",
    "If this code were a novel, it'd be a series of unfortunate events.",
    "This code is like a stubborn lock. It works, but you need to jiggle it a bit.",
    "I've put my blood, sweat, and tears into this code. Mostly tears.",
    "I wrote this using the copy-paste-driven development approach.",
    "This code shall henceforth be known as 'The Forbidden One.'",
    "You don't have to be crazy to understand this code. But it helps.",
    "This is not the code you are looking for. Move along, move along.",
    "This code is a mystery, wrapped in an enigma, and compiled with warnings.",
    "I'm not sure if this code is a genius or insanity. Maybe both.",
    "This code is like a bad penny... it always turns up.",
    "This code is the reason I have trust issues.",
    "I put the 'pro' in procrastinate while writing this function.",
    "This code is a black hole. It's best not to look directly at it.",
    "If you listen closely, you can hear my screams of frustration in each line of this code.",
    "Not to brag, but this code will make history... as a bad example.",
    "This code is like a fossil. It proves that bad practices existed millions of years ago.",
    "I would like to apologize to anyone who has to maintain this code. I was young and needed the commits.",
    "This code is like a puzzle with extra pieces. Good luck!",
    "This code is as mysterious as the dark side of the moon.",
    "Good code is like a good joke: it needs no explanation. So what's this then?",
    "This code is like a good drama - full of unexpected twists.",
    "I followed the 'Road Less Traveled' and now I have no idea where I am in this code.",
    "They say that copy-pasting from Stack Overflow is bad. I agree. Hence, I re-typed it.",
    "This code is like a reality show. It's hard to look away from the disaster.",
    "This code is my spirit animal. It's a little bit messy, but it gets the job done.",
    "I'm not saying that this code is a mess, but the maid quit.",
    "I had a problem, so I used Java. Now I have a ProblemFactory.",
    "This code is the digital equivalent of interpretive dance.",
    "This code is so abstract, it could be an art exhibit.",
    "This is what happens when an unstoppable force meets an immovable object. #CodeBlock",
    "This code is like a diary. It's filled with my errors and regrets.",
    "I was told to stand up and code. Now I have a standing bug.",
    "This code is like a silent movie. It's quaint, but you're not quite sure what's going on.",
    "I tried to make this code self-documenting, but it turned out to be self-destructing.",
    "This code is like a snail. It's slow, but it's carrying its home (of bugs).",
    "This code is like a good thriller. Full of suspense and 'undefined' behavior.",
    "They say don't drink and code. This code is why.",
    "Apologies in advance, future me. I'm sure you'll have fun deciphering this code.",
    "Legend has it that this code was written by a caffeine-fueled unicorn on a quest for world domination.",
    "If you're reading this, you've either stumbled upon a masterpiece or a disaster. No refunds.",
    "I'm not sure what this code does, but it seems to be working. Don't touch it.",
    "This code is like a box of chocolates. You never know what you're gonna get.",
    "This code is so bad, it's not even wrong.",
    "I'm not sure if this is code or a cry for help.",
    "This code is held together with duct tape and prayers. Please handle with care.",
    "May the force be with you, brave soul who ventures to understand this code.",
    "This code is self-documenting. Just kidding, I'm too lazy to write comments.",
    "This code is like a fine wine. It gets better with age. Or maybe it just gets more confusing.",
    "If at first you don't succeed, try coding like a six-year-old. It might just work.",
    "Coding is like painting. Except the paint is invisible and the canvas is a screen that screams at you.",
    "There are two types of people in this world: those who can code and those who can't. And then there's me, who can kind of code, but not really.",
    "I'm not a programmer. I'm just a person who Googles things really well.",
    "Coding is easy. It's like riding a bike. Except the bike is on fire and you're on fire and everything is on fire.",
    "If you see a bug in this code, please squash it. It's probably harmless, but I'm not taking any chances.",
    "This code is dedicated to all the coffee beans that gave their lives to make it possible.",
    "I'm not sure if this code is brilliant or terrible. But it's definitely mine.",
    "This code is like a good joke. It's short, simple, and makes you laugh. Or maybe it just makes you cry.",
    "Coding is like solving a puzzle. Except the puzzle is constantly changing and the pieces are all screaming at you.",
    "If you're not part of the solution, you're part of the precipitate.",
    "This code is proudly sponsored by caffeine and procrastination.",
    "This code is like a haiku. It's short, sweet, and completely incomprehensible.",
    "Coding is like building a house. Except the house is made of code and the foundation is made of bugs.",
    "I'm not a perfectionist. I'm just terrified of bugs.",
    "This code is like a unicorn. It's beautiful, magical, and probably doesn't exist.",
    "Coding is like writing a novel. Except the novel is written in a language that only computers can understand.",
    "I'm not sure what's worse: writing code or reading code.",
    "This code is like a black hole. It's dense, mysterious, and sucks in everything around it.",
    "Coding is like painting a masterpiece. Except the paint is invisible and the canvas is a screen that screams at you.",
    "I'm not a programmer. I'm just a wizard who knows how to make things happen with words.",
    "This code is like a symphony. It's complex, beautiful, and requires a lot of caffeine to appreciate.",
    "Coding is like playing chess. Except the chess pieces are all bugs and the board is on fire.",
    "I'm not sure what I'm doing, but I'm doing it with style.",
    "This code is like a good book. It's hard to put down, but you'll be glad you did.",
    "Coding is like breathing. You don't think about it, you just do it. Unless you're a programmer, in which case you think about it all the time.",
    "If you're reading this, you've ventured too far into the code mines. Turn back now!",
    "I'm not sure what this code does, but it seems to be afraid of the dark. Better leave the lights on.",
    "This code is like a fine wine: it gets better with age. Or maybe it just gets more confusing.",
    "Warning: this code may contain traces of nuts.",
    "I'm not saying this code is perfect, but it's closer to perfect than anything I could have written yesterday.",
    "This code is a work of art. I'm not sure what kind of art, but it's definitely art.",
    "Please don't feed the code after midnight.",
    "This code is like a box of chocolates. You never know what you're gonna get.",
    "I'm not sure if this code is brilliant or just insane. Maybe it's both.",
    "This code is so bad, it's good.",
    "This code is like a unicorn: it's magical, but it doesn't exist.",
    "I'm not sure who wrote this code, but I'm pretty sure they were drunk.",
    "This code is like a labyrinth: it's easy to get lost in, and hard to escape.",
    "This code is so complex, it has its own gravitational pull.",
    "This code is like a black hole: it sucks in everything, and nothing can escape.",
    "This code is like a roller coaster: it's full of twists and turns, and it's sure to make you scream.",
    "This code is like a Rubik's Cube: it's frustrating, but it's also satisfying when you finally solve it.",
    "This code is like a good book: it's hard to put down.",
    "This code is like a bad movie: it's hard to watch, but you can't look away.",
    "This code is like a magic spell. Utter the right incantation, and watch as your program comes to life.",
    "I'm not sure if this code will fix the bug, but it will definitely make it harder to find.",
    "This code is so elegant, it's like watching a ballet performance by the computer.",
    "If this code works, I owe myself a beer. If it doesn't, I owe myself two.",
    "This code is like a Swiss Army knife. It may not be pretty, but it gets the job done.",
    "I'm not a programmer, but I play one on the internet. And in this code.",
    "This code may not be perfect, but at least it's not as bad as Windows Vista.",
    "This code is like a roller coaster. It's full of ups and downs, twists and turns, and sometimes it makes you want to throw up.",
    "This code is like a game of Jenga. One wrong move, and it all comes crashing down.",
    "This code is like a puzzle. It may take some time to figure out, but it's worth it in the end.",
    "I'm not sure what this code does, but it looks important.",
    "This code is like a maze. It may take some time to get through, but there's always a way out.",
    "This code is like a time machine. It takes you back to a simpler time, when programming was fun and not just a job.",
    "I didn't write this code, but I'm pretending I did so I can look smart.",
    "This code is like a Rube Goldberg machine. It may be overly complicated, but it's definitely entertaining.",
]


def add_comment(comment):
    comments_ref = db.collection("comments")
    comments_ref.add({
        "text": comment,
        "posted": None
    })


# Example usage
for comment in comments:
    add_comment(comment)
    print(comment + "added")
