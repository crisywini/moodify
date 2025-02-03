import spotipy
from spotipy import SpotifyOAuth

with open("secrets.txt") as file:
    client_id = file.readline().strip()
    client_secret = file.readline().strip()

print(client_id)
print(client_secret)


redirect_uri = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read"))

#current_user = sp.current_user()
#print(current_user)

music_found = sp.search(q="Happy songs", limit=4, type="track")
print(music_found)