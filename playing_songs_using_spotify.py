# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# # Set up the Spotify API client
# scope = "user-read-playback-state,user-modify-playback-state"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#
# def play_song(song_uri):
#     # Start playback of the specified track
#     sp.start_playback(uris=[song_uri])
#
# if __name__ == "__main__":
#     # Example song URI
#     song_uri = "spotify:track:6rqhFgbbKwnb9MLmUQDhG6"  # Replace with your desired song URI
#
#     # Play the song
#     play_song(song_uri)



import openai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up your OpenAI API key
openai.api_key = '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'

# Set up your Spotify API credentials
spotify_client_id = 'YOUR_SPOTIFY_CLIENT_ID'
spotify_client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'

# Authenticate with Spotify API
spotify_client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id,
                                                              client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=spotify_client_credentials_manager)


def search_song(song_name):
    # Call OpenAI's API to generate a search query prompt
    prompt = f"Find the song '{song_name}' on Spotify."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    # Extract the generated search query
    search_query = response.choices[0].text.strip()

    # Search for the song on Spotify
    results = sp.search(q=search_query, limit=1)
    if results and results['tracks'] and results['tracks']['items']:
        track = results['tracks']['items'][0]
        print(f"Found the song '{track['name']}' by {track['artists'][0]['name']} on Spotify.")
        return track['external_urls']['spotify']
    else:
        print("Song not found on Spotify.")


# Example usage
song_name = input("Enter the name of the song you want to find on Spotify: ")
spotify_url = search_song(song_name)
if spotify_url:
    print("You can listen to it on Spotify here:", spotify_url)
