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
    "// I apologize in advance for this code - blame it on Monday morning and too much coffee.",
    "// This code is like a magic spell. Utter the right incantation, and watch as your program comes to life.",
    "// This code is like a symphony of code. Each line plays its own note, coming together to create a beautiful composition.",
    "// This code is like a Rubik's Cube. It challenges your problem-solving skills and twists your mind.",
    "// This code is like a time-lapse of a flower blooming. With each execution, it unfolds its beauty.",
    "// This code is like a hidden treasure. Dive into its logic and uncover the valuable gems it holds.",
    "// This code is like a roller coaster ride. Hold on tight, and enjoy the exhilarating ups and downs of debugging.",
    "// Get ready for the code extravaganza that will leave you in awe of its complexity.",
    "// Step into the realm of code dreams and witness the impossible come to life.",
    "// Brace yourself for the code masterpiece that will redefine your understanding of elegance.",
    "// Prepare to be amazed by the code symphony that harmonizes data and logic.",
    "// Hold your breath as this code paints a picture of efficiency and elegance.",
    "// This code is like a jigsaw puzzle. Each line is a piece, and putting them together completes the picture.",
    "// This code is like a zen garden. Its clean and well-structured logic brings peace and serenity to the development process.",
    "// This code is like a quantum computer. It harnesses the power of superposition and entanglement to solve complex problems.",
    "// This code is like a magic spell. Utter the right incantation, and watch as your program comes to life.",
    "// TODO: Refactor this mess into something that doesn't make me question my life choices.",
    "// This code is like a box of chocolates, you never know what you're gonna get (unless you debug it).",
    "// If you're reading this, it means I'm probably not working here anymore. Good luck fixing my code!",
    "// WARNING: Abandon all hope, ye who enter here. The code below is a labyrinth of despair.",
    "// TODO: Write a witty comment here, because the code speaks for itself and it's not saying anything nice.",
    "// Congratulations! You've found the unicorn of code. It actually works.",
    "// Don't touch this code with a ten-foot pole. I'm not responsible for any headaches it may cause.",
    "// WARNING: This code has been possessed by the ghost of a junior developer. Proceed with caution.",
    "// I'm not lazy, I'm just conserving energy. This code is optimized for maximum nap time.",
    "// I coded this while I was half-asleep. Good luck trying to decipher it!",
    "// In case of emergency, break glass and blame the intern.",
    "// I have CDO. It's like OCD, but with the letters in the correct alphabetical order. Just like this code.",
    "// I solemnly swear that I'm up to no good. Proceed with caution.",
    "// This code is like a roller coaster ride. Buckle up and hold on tight!",
    "// You've reached the end of the code. Congratulations! Your reward is... more code.",
    "// This function is as useless as a white crayon. It exists, but no one knows why.",
    "// Please forgive the messiness of this code. My cat walked across the keyboard.",
    "// This code is so old, it's practically written in hieroglyphics.",
    "// WARNING: This code may contain traces of nuts. Proceed with care.",
    "// This code is like a toddler on a sugar rush. It's unpredictable and will probably break something.",
    "// Don't worry, I left a few bugs in this code as pets. They're harmless, I promise.",
    "// This code is a work of art. Picasso would be proud (or horrified).",
    "// This function is like a black hole. It takes in data and never returns anything.",
    "// This code is like a cat: it only works when it feels like it.",
    "// I'm sorry, future developer, for what you're about to experience. Godspeed!",
    "// This code is my baby. It's cute, but it keeps me up all night.",
    "// This code is like a potato. It's not pretty, but it gets the job done.",
    "// This code is proof that I have a sense of humor. I hope you do too.",
    "// Do not meddle in the affairs of this code, for it is subtle and quick to anger.",
    "// This code is like a bad pun. It's painful, yet strangely amusing.",
    "// The only thing missing from this code is a \"Ta-da!\" at the end.",
    "// This code is like a soap opera. It's full of drama, unexpected twists, and bugs.",
    "// WARNING: The code below is certified to make your brain explode. Proceed with caution.",
    "// This code is a masterpiece of obfuscation. Good luck trying to decipher my genius.",
    "// This function is like a ninja. It sneaks in, does its job, and disappears without a trace.",
    "// This code is like a time machine. It takes you back to the 90s when spaghetti code ruled the land.",
    "// This code is like a cryptic crossword puzzle. Solve it and earn the respect of your peers.",
    "// Please do not feed the code. It has a tendency to grow uncontrollably.",
    "// This code is like a Rubik's Cube. It looks simple, but it will twist your mind.",
    "// This function is as elusive as a unicorn. I heard it exists, but I've never",
    "// This code is proof that I have a love-hate relationship with programming.",
    "// This code is like a Picasso painting - it's abstract, and only the developer knows what it means.",
    "// This code is like a roller coaster ride without safety belts. Hold on tight and pray for no crashes!",
    "// This code is like a magic trick. It may not make sense, but it somehow produces the right output.",
    "// This code is like a tangled ball of yarn. Good luck unraveling its mysteries.",
    "// This code is like a choose-your-own-adventure book. Every execution path leads to a different outcome.",
    "// May the bugs be ever in your favor!",
    "// Caution: Proceed with a sense of humor. This code enjoys a good joke.",
    "// Unlock the hidden potential of this code and unleash its power!",
    "// Get ready to witness the dance of bytes and bits in this masterpiece.",
    "// This code is like a jigsaw puzzle missing half the pieces. It's frustrating but strangely satisfying when it finally comes together.",
    "// This code is like a deep philosophical question. It raises more questions than it answers.",
    "// This code is like a Rube Goldberg machine. It's overly complex and utterly unnecessary.",
    "// This function is a multitasker. It does so many things at once, you'll need a map to navigate its logic.",
    "// This function is like a diva. It demands attention and refuses to play well with others.",
    "// This function is a wild goose chase. It takes you on a journey with no destination in sight.",
    "// This function is like a mischievous gremlin. It wreaks havoc when you least expect it.",
    "// This function is a master of disguise. It pretends to be useful, but deep down, it's just playing tricks on you.",
    "// This function is a real-life \"Inception\" dream. Layers upon layers of complexity, leaving you questioning your sanity.",
    "// This class is like a well-orchestrated ballet. Each method dances in harmony, creating a beautiful performance.",
    "// This class is a mysterious book of ancient spells. Its methods hold secrets that only the chosen ones can understand.",
    "// This class is a time traveler. It carries the legacy of past code, adapted to survive in the ever-changing present.",
    "// This class is a wise old sage. Its methods hold wisdom accumulated through years of coding.",
    "// Patched the bug that turned the application into a virtual haunted house. Ghosts are now strictly prohibited.",
    "// Fixed the bug that caused the database to play hide and seek. Now it's always ready to reveal its secrets.",
    "// Bug defeated! The infinite loop that sent the program into a time warp has been terminated. Time can now flow freely.",
    "// Fixed the bug that made the text look like it was straight out of a Salvador Dali painting. It's now back to being readable and sane.",
    "// Patched the bug that turned the colors into a psychedelic rainbow. The visuals are now in harmony with the laws of nature.",
    "// Bug neutralized! The self-destruct sequence that triggered every time a user pressed the \"Save\" button has been disarmed.",
    "// This code is as unpredictable as a box of chocolates. You never know what you're gonna get.",
    "// This code is like a secret agent. It operates undercover, silently accomplishing its mission.",
    "// This code is like a symphony conductor. It orchestrates different components to create a harmonious performance.",
    "// This code is like a time capsule. It captures the essence of a bygone era, preserved for future generations.",
    "// This code is a roller coaster for your brain. Get ready for twists, turns, and code-induced adrenaline rushes.",
    "// This code is like a well-written novel. Each line tells a story, drawing you deeper into its narrative.",
    "// This code is like a parallel universe. It mirrors reality, but with its own set of rules and possibilities.",
    "// This code is like a magician's hat. It holds surprises and hidden tricks at every turn.",
    "// This code is like a linguistic puzzle. Unravel its syntax and semantics to reveal its true meaning.",
    "// This code is like a phoenix rising from the ashes. It's been refactored, reborn, and ready to soar.",
    "// This code is like a treasure map. Follow its logic to discover the hidden gems within.",
    "// This code is like a cosmic dance. Its algorithms gracefully move in sync, creating a mesmerizing spectacle.",
    "// This code is like a cat. It's both elegant and unpredictable, with a touch of mischief.",
    "// Step into the code dimension where creativity and logic merge to create miracles.",
    "// Brace yourself for the code tornado that will sweep you off your feet.",
    "// Prepare for a coding adventure that will leave you breathless and craving for more.",
    "// Hold your breath as this code defies expectations and redefines what is possible.",
    "// Get ready to witness the code revolution that will change the way you think about programming.",
    "// This code is like a GPS for the mind. It navigates through complex logic to guide you to the desired destination.",
    "// This code is like a time-lapse video. It captures the evolution of a program, frame by frame.",
    "// This code is like a game of chess. Every move counts, and strategy is key to victory.",
    "// This code is like a riddle waiting to be solved. Crack its secrets and earn the satisfaction of a job well done.",
    "// This code is like a LEGO set. Each function is a brick, and together they build something amazing.",
    "// This code is like a fireworks display. It's a symphony of colors and logic that dazzles the mind.",
    "// This code is like a linguistic fusion. It blends different programming languages into a harmonious whole.",
    "// This code is like a superhero's cape. It empowers you to do extraordinary things with just a few lines.",
    "// This code is like a coffee machine. It brews efficiency and productivity with every run.",
    "// Buckle up, we're about to embark on a wild coding adventure!",
    "// Brace yourself for the mind-bending logic that lies ahead.",
    "// Hold on tight, we're about to take off to programming wonderland.",
    "// This code is like a mirror maze. Reflections of logic lead to paths both mesmerizing and perplexing.",
    "// This code is like a stand-up comedian. It keeps you entertained while delivering its punchlines of functionality.",
    "// This code is like a marathon runner. It's built to go the distance, tackling challenges along the way.",
    "// This code is like a recipe book. Its methods are the ingredients, and executing them creates a delicious result.",
    "// This code is like a linguistic codebreaker. Decrypt its language to unlock its full potential.",
    "// This code is like a sculptor's masterpiece. Each line shapes the final form, revealing its true beauty.",
    "// This code is like a hacker's playground. It pushes the boundaries of what's possible, exploring new frontiers.",
    "// This code is like a virtual reality experience. Immerse yourself in its logic and explore a digital world.",
    "// This code is like a cosmic tapestry. Its patterns intertwine, creating a universe of functionality.",
    "// This code is like a stand-up magician. It combines humor and sleight of hand to surprise and delight.",
    "// This code is like a crossword puzzle. Solve its clues to uncover the solution to a programming challenge.",
    "// This code is like a time machine. Step into its logic and journey through the past, present, and future.",
    "// This code is like a game of hide and seek. The bugs hide, and your mission is to find and fix them.",
    "// Step right up and witness the magic of this code.",
    "// Prepare to have your mind blown by the awesomeness of this function.",
    "// Don't blink or you might miss the genius of this algorithm.",
    "// This code is like a mad scientist's experiment. It's a fusion of innovation and curiosity, with unpredictable results.",
    "// This code is like a perfectly balanced equation. Its logic maintains order and stability.",
    "// This code is like a magic wand. Wave it, and watch as your desired outcomes materialize.",
    "// This code is like a labyrinth. It's easy to get lost, but with careful navigation, the exit is within reach.",
    "// This code is like a work of art. Its structure and elegance inspire awe and admiration.",
    "// This code is like a game of Tetris. Each line of code fits together, creating a solid and complete structure.",
    "// This code is like a gentle breeze. It flows smoothly, bringing a sense of calmness to the development process.",
    "// This code is like a garden. Nurture it with care, and watch as your codebase blossoms.",
    "// Get ready to embark on a quest to tame the wild beast called code.",
    "// Enter the code labyrinth and see if you can find the way out.",
    "// Caution: This code has a mischievous sense of humor. Brace yourself for unexpected outcomes.",
    "// Prepare for the code symphony that will serenade your senses.",
    "// Hold your breath as this code performs its breathtaking acrobatics.",
    "// This code is like a DJ's mixtape. It seamlessly blends different components to create a unified experience.",
    "// This function is a rebel without a cause. It doesn't follow any coding conventions and does things its own way.",
    "// This function is a stealthy ninja. It silently executes its tasks, leaving no trace behind.",
    "// This function is like a carnival game. It promises a prize, but you always end up with a stuffed animal you don't want.",
    "// This class is a gathering of code wizards. Enter with awe and be prepared to witness magic.",
    "// This class is like a rock band. Each method plays its own instrument, creating a symphony of functionality.",
    "// This class is the Dumbledore of the codebase. Wise, powerful, and a little eccentric.",
    "// This class is a superhero team. Each method has its own superpower, combining forces to save the day.",
    "// This class is a treasure chest. Open it, and you'll find gems of functionality waiting to be discovered.",
    "// This code is like a well-oiled machine. It operates flawlessly, with efficiency and precision.",
    "// This code is like a black hole. Once you enter its logic, there's no escape from its gravitational pull.",
    "// This code is like a ninja warrior. It moves swiftly and silently, executing tasks with deadly precision.",
    "// This code is like a virtual pet. It needs constant attention and care to thrive and perform well.",
    "// Fasten your seatbelt, this code is about to defy gravity.",
    "// Prepare for a coding experience like no other. It's time to push the boundaries.",
    "// Get ready for the code fireworks that will light up your screen.",
    "// Prepare to be amazed by the code symphony that harmonizes data and logic.",
    "// Hold on tight as this code unleashes its power, transforming complexity into simplicity.",
    "// This code is like a trailblazer. It pushes the boundaries of what's possible and paves the way for innovation.",
    "// This code is like a symphony of code. Each line plays its own note, coming together to create a beautiful composition.",
    "// This code is like a Rubik's Cube. It challenges your problem-solving skills and twists your mind.",
    "// This code is like a time-lapse of a flower blooming. With each execution, it unfolds its beauty.",
    "// This code is like a hidden treasure. Dive into its logic and uncover the valuable gems it holds.",
    "// This code is like a roller coaster ride. Hold on tight, and enjoy the exhilarating ups and downs of debugging.",
    "// This code is like a jigsaw puzzle. Each line is a piece, and putting them together completes the picture.",
    "// This code is like a zen garden. Its clean and well-structured logic brings peace and serenity to the development process.",
    "// This code is like a quantum computer. It harnesses the power of superposition and entanglement to solve complex problems.",
    "// This code is like a magician's hat. It holds surprises and hidden tricks at every turn.",
    "// Step into the world of code magic and witness the impossible become possible.",
    "// Brace yourself for the code avalanche that will challenge your problem-solving skills.",
    "// Prepare for a code journey that will test your limits and expand your horizons.",
    "// Hold on tight as this code takes you on a thrilling ride through its logic.",
    "// Get ready for the code extravaganza that will leave you in awe of its complexity.",
    "// Step into the realm of code dreams and witness the impossible come to life.",
    "// Brace yourself for the code masterpiece that will redefine your understanding of elegance.",
    "// This code is like a labyrinth. It's easy to get lost, but with careful navigation, the exit is within reach.",
    "// This code is like a DJ's mixtape. It seamlessly blends different components to create a unified experience.",
    "// This code is like a well-oiled machine. It operates flawlessly, with efficiency and precision.",
    "// This code is like a black hole. Once you enter its logic, there's no escape from its gravitational pull.",
    "// This code is like a ninja warrior. It moves swiftly and silently, executing tasks with deadly precision.",
    "// This code is like a virtual pet. It needs constant attention and care to thrive and perform well.",
    "// This code is like a trailblazer. It pushes the boundaries of what's possible and paves the way for innovation.",
    "// Hold your breath as this code paints a picture of efficiency and elegance.",
    "// Get ready to be captivated by the code ballet that elegantly executes its steps.",
    "// Step into the code wonderland where imagination meets logical brilliance.",
    "// Brace yourself for the code fireworks that will light up your development process.",
    "// Prepare for a coding experience that will challenge your skills and ignite your passion.",
    "// This code is like a symphony of code. Each line plays its own note, coming together to create a beautiful composition.",
    "// This code is like a Rubik's Cube. It challenges your problem-solving skills and twists your mind.",
    "// This code is like a time-lapse of a flower blooming. With each execution, it unfolds its beauty.",
    "// This code is like a hidden treasure. Dive into its logic and uncover the valuable gems it holds.",
    "// This code is like a roller coaster ride. Hold on tight, and enjoy the exhilarating ups and downs of debugging.",
    "// This code is like a jigsaw puzzle. Each line is a piece, and putting them together completes the picture.",
    "// This code is like a zen garden. Its clean and well-structured logic brings peace and serenity to the development process.",
    "// This code is like a quantum computer. It harnesses the power of superposition and entanglement to solve complex problems.",
    "// This code is like a magic spell. Utter the right incantation, and watch as your program comes to life.",
    "// Brace yourself for the roller coaster ride of code execution.",
    "// Dive into the rabbit hole of this code and discover its secrets.",
    "// Get ready to be dazzled by the code spectacle that defies conventional thinking.",
    "// Step into the code laboratory where innovation is born and breakthroughs happen.",
    "// Brace yourself for the code tsunami that will wash away complexity and bring clarity.",
    "// Prepare for a coding journey that will push your boundaries and expand your horizons.",
    "// Hold on tight as this code takes you on a thrilling ride through its logic.",
    "// Get ready to be captivated by the code ballet that elegantly executes its steps."
]


def add_comment(comment):
    comments_ref = db.collection("comments")
    comments_ref.add({
        "text": comment,
        "flag": None
    })


# Example usage
for comment in comments:
    add_comment(comment)
    print(comment + "added")
