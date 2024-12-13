from pprint import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# move_to_date = input("Which year you want to travel to? Type date in format YYYY-MM-DD")
move_to_date = "2000-08-12"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = f"https://www.billboard.com/charts/hot-100/{move_to_date}"

response = requests.get(url=URL, headers=header)
# print(response.raise_for_status()) # will return error if cant reach response
bb_content = response.text

soup = BeautifulSoup(bb_content, "html.parser")
# print(soup.title)   # test

# all_song_titles = soup.find_all(name="h3", id_="title-of-a-story")
#
# for song_title in all_song_titles:
#     print(song_title.getText()[0])
# all_song_titles = soup.select_one(selector="h3 #id")
# all_song_titles = soup.find(name="h3")
# print(all_song_titles)

# all_songs_content = soup.find_all(name="a", class_="c-title__link lrv-a-unstyle-link")
# print(first_song.getText().strip())



# all_songs_content = soup.find_all(name="h3", class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150")
# print(all_songs_content.getText().strip())

# partial_class_string = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021"
# all_anchor_links = soup.find_all(name="a")
# # for a_link in all_anchor_links:
# if partial_class_string in all_anchor_links:
#     print(all_anchor_links)
#
# print(all_anchor_links)

# all_song_titles = [song.getText().strip() for song in all_songs_content]
# print(all_song_titles)

song_names_spans = soup.select("li ul li h3")
all_song_titles = [song.getText().strip() for song in song_names_spans]
print(all_song_titles)

#### SPOTIFY; username: k3054294@gmail.com (sing in with google)
spotify_client_id = "536e1d2edddb49ed94924e71851687a4"
spotify_client_secret = "5be3a18eebfb457fb64f041eb4a154c7"
spotify_redirect_uri= "http://example.com"

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))
# print(sp.raise_for_status)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=spotify_redirect_uri,
                                               scope="playlist-modify-private playlist-read-private"))

# results = sp.search(q='weezer', limit=5)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

results = sp.current_user_saved_tracks()
# print(results)    # test, result:
## {'href': 'https://api.spotify.com/v1/me/tracks?offset=0&limit=20', 'items': [{'added_at': '2024-11-15T11:40:31Z', 'track': {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4UXJsSlnKd7ltsrHebV79Q'}, 'href': 'https://api.spotify.com/v1/artists/4UXJsSlnKd7ltsrHebV79Q', 'id': '4UXJsSlnKd7ltsrHebV79Q', 'name': 'Nick Cave & The Bad Seeds', 'type': 'artist', 'uri': 'spotify:artist:4UXJsSlnKd7ltsrHebV79Q'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'external_urls': {'spotify': 'https://open.spotify.com/album/0DpHNtdQBy3e2Iy6TKLWIv'}, 'href': 'https://api.spotify.com/v1/albums/0DpHNtdQBy3e2Iy6TKLWIv', 'id': '0DpHNtdQBy3e2Iy6TKLWIv', 'images': [{'height': 640, 'width': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27388f436c4a60e459f793f7b74'}, {'height': 300, 'width': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0288f436c4a60e459f793f7b74'}, {'height': 64, 'width': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485188f436c4a60e459f793f7b74'}], 'is_playable': True, 'name': "The Boatman's Call (2011 - Remaster)", 'release_date': '1997-03-03', 'release_date_precision': 'day', 'total_tracks': 12, 'type': 'album', 'uri': 'spotify:album:0DpHNtdQBy3e2Iy6TKLWIv'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4UXJsSlnKd7ltsrHebV79Q'}, 'href': 'https://api.spotify.com/v1/artists/4UXJsSlnKd7ltsrHebV79Q', 'id': '4UXJsSlnKd7ltsrHebV79Q', 'name': 'Nick Cave & The Bad Seeds', 'type': 'artist', 'uri': 'spotify:artist:4UXJsSlnKd7ltsrHebV79Q'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'disc_number': 1, 'duration_ms': 256120, 'explicit': False, 'external_ids': {'isrc': 'GBAJH1000649'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/39CFOvYse9fcMhIwyS73Fl'}, 'href': 'https://api.spotify.com/v1/tracks/39CFOvYse9fcMhIwyS73Fl', 'id': '39CFOvYse9fcMhIwyS73Fl', 'is_local': False, 'is_playable': True, 'name': 'Into My Arms', 'popularity': 63, 'preview_url': 'https://p.scdn.co/mp3-preview/3129c67e60f0a5a5f478b2be5df10d3fd025d15c?cid=536e1d2edddb49ed94924e71851687a4', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:39CFOvYse9fcMhIwyS73Fl'}}], 'limit': 20, 'next': None, 'offset': 0, 'previous': None, 'total': 1}
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

user_info = sp.current_user()   # https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user
print(user_info['display_name']) # k3054294

print(user_info["id"]) # 31fwkgbvdqn4prk7yhphkbxvxvjy


#  SEARCH FOR TRACK:https://developer.spotify.com/documentation/web-api/reference/search

song_ids = []
for song in all_song_titles:
    song_searched = sp.search(q=f"track: {song} year: {int(move_to_date[0:4])}", type="track", market="IE")["tracks"]["items"][0]["uri"]
    try:
        song_ids.append(song_searched)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# song_id = sp.search("Incomplete")
pprint(song_ids[:2])
print(len(song_ids))

# NEXT STEPS?
"""1. Using the Spotipy documentation, create a new private playlist with the name "YYYY-MM-DD Billboard 100", 
where the date is the date you inputted in step 1.
HINT: You'll need the user id you got from Step 2.
2. Add each of the songs found in Step 3 to the new playlist.
HINT: You'll need the playlist id which is returned as an output once you've successfully created a new playlist."""
# https://spotipy.readthedocs.io/en/2.24.0/#spotipy.client.Spotify.user_playlist_create
# https://spotipy.readthedocs.io/en/2.24.0/#spotipy.client.Spotify.playlist_add_items



create_bb_playlist = sp.user_playlist_create(user=user_info["id"], name=f"{move_to_date} Billboard 100", public=False)
print(create_bb_playlist)
# if "id" not in user_playlist(user, playlist_id=None, fields=None, market=None):
# playlists = sp.user_playlists(user=user_info["id"])

# #to get all existing playlists Ids - this was not needed - I think it would throw an error if the playlist exists:
# existing_playlists_ids = []
# for i in enumerate(playlists["items"]):
#     existing_playlists_ids.append(i[1]["id"])

# print(existing_playlists_ids)

# if id not in existing_playlists_ids:
#     create_bb_playlist = sp.user_playlist_create(user=user_info["id"], name=f"{move_to_date} Billboard 100", public="True")
sp.playlist_add_items(playlist_id=create_bb_playlist["id"], items=song_ids)
