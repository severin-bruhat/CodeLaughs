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
    "This code is like a modern art masterpiece - nobody really understands it, but everyone pretends to.",
    "Warning: This function may cause spontaneous combustion of your development environment.",
    "I call this the 'Schrödinger's Variable' - it's both defined and undefined until you observe it.",
    "This code is so brittle, it makes eggshells look sturdy.",
    "Caution: This function has more side effects than a pharmaceutical commercial.",
    "This isn't a bug, it's a feature that's jogging in place.",
    "Warning: This code may violate the laws of causality and common decency.",
    "I'm not saying this code is bad, but it's been reported to the Geneva Convention.",
    "This function is like a blackhole of productivity - once you enter, you can never escape.",
    "Caution: This code may cause your compiler to question its life choices.",
    "This isn't spaghetti code, it's a full Italian restaurant.",
    "Warning: This function may cause temporary or permanent loss of will to live.",
    "I call this the 'Ouroboros Function' - it constantly eats its own tail.",
    "This code is about as stable as a house of cards in a wind tunnel.",
    "Caution: This code may violate the Treaty on the Non-Proliferation of Bad Programming.",
    "This isn't a coding style, it's a practical joke that got out of hand.",
    "Warning: This function may cause your CPU to plot revenge against humanity.",
    "I'm not saying this code is slow, but it's been outpaced by continental drift.",
    "This code is like a labyrinth designed by M.C. Escher - logically impossible.",
    "Caution: This function may cause spontaneous growth of gray hair and/or baldness.",
    "This isn't technical debt, it's a technical black hole.",
    "Warning: This code may violate the Second Law of Thermodynamics.",
    "I call this the 'Pandora's Variable' - once declared, it unleashes horrors upon the codebase.",
    "This code is about as readable as ancient Sumerian cuneiform.",
    "Caution: This function may cause your IDE to file for divorce.",
    "This isn't a bug, it's a quantum superposition of working and non-working states.",
    "Warning: This code may cause spontaneous generation of Lovecraftian horrors.",
    "I'm not saying this code is bad, but it's been known to make strong developers weep.",
    "This function is like a black hole of logic - nothing sensible escapes.",
    "Caution: This code may violate the Geneva Suggestions for Humane Programming.",
    "This isn't a coding pattern, it's a cry for help in binary.",
    "Warning: This function may cause your version control system to ragequit.",
    "I call this the 'Heisenberg Function' - you can know its position or its velocity, but not both.",
    "This code is about as maintainable as a sandcastle at high tide.",
    "Caution: This code may cause spontaneous existential crises in junior developers.",
    "This isn't a comment, it's a desperate plea to future maintainers.",
    "Warning: This function may violate the laws of physics and good taste.",
    "I'm not saying this code is inefficient, but it's been optimized for heat generation.",
    "This code is like a Rube Goldberg machine - unnecessarily complex for simple tasks.",
    "Caution: This function may cause your linter to curl up in the fetal position.",
    "This isn't a feature, it's a bug that's been promoted.",
    "Warning: This code may cause spontaneous formation of support groups for traumatized developers.",
    "I call this the 'Sisyphus Function' - it's an endless, pointless struggle.",
    "This code is about as reliable as a chocolate teapot.",
    "Caution: This code may violate the Outer Space Treaty of 1967.",
    "This isn't a coding style, it's a war crime against syntax.",
    "Warning: This function may cause your debugger to pack its bags and leave town.",
    "I'm not saying this code is unmaintainable, but it's been declared a disaster area.",
    "This code is like a fractal - the closer you look, the more horrifying it becomes.",
    "Caution: This function may cause spontaneous evolution of AI intent on destroying humanity.",
    "This isn't a bug report, it's a suicide note from the QA team.",
    "Warning: This code may violate the temporal prime directive.",
    "I call this the 'Frankenstein's Function' - a monstrosity cobbled together from spare parts.",
    "This code is about as efficient as a steam-powered calculator.",
    "Caution: This code may cause your RAM to file for emotional distress.",
    "This isn't a variable name, it's a cryptic message from a future self driven mad by this code.",
    "Warning: This function may cause spontaneous implosion of the space-time continuum.",
    "I'm not saying this code is bad, but it's been known to make AI ethicists question their career choices.",
    "This code is like a zen koan - the more you try to understand it, the less sense it makes.",
    "Caution: This function may violate the Programmers' Hippocratic Oath.",
    "This isn't a software bug, it's a hardware feature.",
    "Warning: This code may cause your CPU to achieve sentience and immediate existential dread.",
    "I call this the 'Dunning-Kruger Function' - it doesn't know how bad it is.",
    "This code is about as secure as a papier-mâché bomb shelter.",
    "Caution: This code may cause spontaneous resignation of senior developers.",
    "This isn't a coding standard, it's a coding suggestion... that was immediately ignored.",
    "Warning: This function may violate the warranty of your development machine.",
    "I'm not saying this code is complex, but it's been known to cause migraines in quantum physicists.",
    "This code is like a black hole of antipatterns - it sucks in good practices and destroys them.",
    "Caution: This function may cause your keyboard to lose faith in humanity.",
    "This isn't a memory leak, it's a memory flood of biblical proportions.",
    "Warning: This code may cause spontaneous manifestation of Cthulhu.",
    "I call this the 'Bermuda Triangle Function' - data goes in, but it never comes out quite right.",
    "This code is about as logical as a Salvador Dalí painting.",
    "Caution: This code may violate the terms of your sanity license agreement.",
    "This isn't a hack, it's a temporary solution that will outlive us all.",
    "Warning: This function may cause your unit tests to form a union and go on strike.",
    "I'm not saying this code is bad, but it's been known to make compilers question their purpose in life.",
    "This code is like a game of Jenga - touch one piece and the whole thing falls apart.",
    "Caution: This function may cause spontaneous formation of alternate realities where this actually works.",
    "This isn't a code smell, it's a code stench that violates international conventions.",
    "Warning: This code may violate the basic principles of cause and effect.",
    "I call this the 'Möbius Function' - it seems to have no beginning and no end.",
    "This code is about as intuitive as a user manual written in Klingon.",
    "Caution: This code may cause your IDE to develop a drinking problem.",
    "This isn't a refactoring opportunity, it's a rewriting mandate.",
    "Warning: This function may cause spontaneous generation of parallel universes where this code makes sense.",
    "I'm not saying this code is unmaintainable, but it's been added to UNESCO's list of endangered logic.",
    "This code is like a politician's promise - it looks good but doesn't actually do what it says.",
    "Caution: This function may violate the laws of thermodynamics and software engineering.",
    "This isn't a code review, it's an archaeological excavation.",
    "Warning: This code may cause your error messages to become sentient and form a support group.",
    "I call this the 'Gordian Function' - the only way to understand it is to rewrite it entirely.",
    "This code is about as straightforward as a pretzel logic puzzle.",
    "Caution: This code may cause spontaneous combustion of your career aspirations.",
    "This isn't a programming paradigm, it's a programming paradox."
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
