import random

jokes_data = []
joke_list = [
    "Miss You: Oliver Tree",
    "Poland: Lil Yachty",
    "NOSTYLIST: Destroy Lonely",
    "you're a parasite: Riovaz",
    "505: Artic Monkeys",
    "Me and Your Mama: Childish Gambino",
    "Let It Happen: Tame Impala",
    "Dark Fantasy: Kanye",
    "Bad Habit: Steve Lacy",
    'Super Freaky Girl: Nicki Minaj'
]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in joke_list:
        jokes_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(jokes_data)

# Joke getter
def getJoke(id):
    return(jokes_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(jokes_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return jokes_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return jokes_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    jokes_data[id]['haha'] = jokes_data[id]['haha'] + 1
    return jokes_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    jokes_data[id]['boohoo'] = jokes_data[id]['boohoo'] + 1
    return jokes_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(jokes_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))