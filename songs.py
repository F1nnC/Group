import random

# the list of data
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

# Initialize Songs
def initSongs():
    # setup songs into a dictionary with id, song, like, dislike
    item_id = 0
    for item in song_list:
        songs_data.append({"id": item_id, "song": item, "like": 0, "dislike": 0})
        item_id += 1
    # prime some like responses
    for i in range(10):
        id = getRandomSongs()['id']
        addSongLike(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomSongs()['id']
        addSongDislike(id)
        
# Return all songs from songs_data
def getSongs():
    return(songs_data)

# song getter
def getSong(id):
    return(songs_data[id])

# Return random song from songs_data
def getRandomSongs():
    return(random.choice(songs_data))

# Liked song
def favoriteSong():
    best = 0
    bestID = -1
    for songs in getSongs():
        if songs['like'] > best:
            best = songs['like']
            bestID = songs['id']
    return songs_data[bestID]
    
# Liked song
def DislikeSong():
    worst = 0
    worstID = -1
    for song in getSongs():
        if song['dislike'] > worst:
            worst = song['dislike']
            worstID = song['id']
    return songs_data[worstID]

# Add to like for requested id
def addSongLike(id):
    songs_data[id]['like'] = songs_data[id]['like'] + 1
    return songs_data[id]['like']

# Add to dislike for requested id
def addSongDislike(id):
    songs_data[id]['dislike'] = songs_data[id]['dislike'] + 1
    return songs_data[id]['dislike']

# Pretty Print Song
def printSong(song):
    print(song['id'], song['song'], "\n", "Like:", song['like'], "\n", "Dislike:", song['dislike'], "\n")

# Number of song
def countSongs():
    return len(songs_data)

# Test Song Model
if __name__ == "__main__": 
    initSongs()  # initialize song
    
    # Most likes and disliked
    best = favoriteSong()
    print("Most liked", best['like'])
    printSong(best)
    worst = DislikeSong()
    print("Most Dislike", worst['dislike'])
    printSong(worst)
    
    # Random song
    print("Random Song")
    printSong(getRandomSongs())
    
    # Count of Song
    print("Song Count: " + str(countSongs()))