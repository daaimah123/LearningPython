# find total time duration of music playlist

playlist = {
    'title': 'Studying Python', 
    'author': 'Daaimah Tibrey', 
    'songs': [
        {'title': 'song1', 
        'artist': 'artist1', 
        'duration': 3.0
        },
        {'title': 'song2', 
        'artist': 'artist2', 
        'duration': 3.5 
        },
        {'title': 'song3', 
        'artist': 'artist3', 
        'duration': 2.4
        },
    ]
}

total = 0
for song in playlist['songs']:
    total+=song['duration']
print(total)