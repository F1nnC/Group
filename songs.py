import random

songs_data = []
song_list = [
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
def initSongs():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in song_list:
        songs_data.append({"id": item_id, "song": item, "like": 0, "dislike": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomSongs()['id']
        addSongLike(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomSongs()['id']
        addSongDislike(id)
        
# Return all jokes from jokes_data
def getSongs():
    return(songs_data)

# Joke getter
def getSong(id):
    return(songs_data[id])

# Return random joke from jokes_data
def getRandomSongs():
    return(random.choice(songs_data))

# Liked joke
def favoriteSong():
    best = 0
    bestID = -1
    for songs in getSongs():
        if songs['like'] > best:
            best = songs['like']
            bestID = songs['id']
    return songs_data[bestID]
    
# Jeered joke
def DislikeSong():
    worst = 0
    worstID = -1
    for song in getSongs():
        if song['dislike'] > worst:
            worst = song['dislike']
            worstID = song['id']
    return songs_data[worstID]

# Add to haha for requested id
def addSongLike(id):
    songs_data[id]['like'] = songs_data[id]['like'] + 1
    return songs_data[id]['like']

# Add to boohoo for requested id
def addSongDislike(id):
    songs_data[id]['dislike'] = songs_data[id]['dislike'] + 1
    return songs_data[id]['dislike']

# Pretty Print joke
def printJoke(song):
    print(song['id'], song['song'], "\n", "Like:", song['like'], "\n", "Dislike:", song['dislike'], "\n")

# Number of jokes
def countSongs():
    return len(songs_data)

# Test Joke Model
if __name__ == "__main__": 
    initSongs()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteSong()
    print("Most liked", best['like'])
    printJoke(best)
    worst = DislikeSong()
    print("Most Dislike", worst['dislike'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomSongs())
    
    # Count of Jokes
    print("Song Count: " + str(countSongs()))