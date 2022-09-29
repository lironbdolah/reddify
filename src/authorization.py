import re
import spotipy
import spotipy.util as util
import json
import requests


def add_tracks(username,subreddit,category,limit,date_range,token,playlist_id):

    sp = spotipy.Spotify(auth=token)
    tracks_ids = []

    # get url
    try:
        URL = f'https://www.reddit.com/r/{subreddit}/{category}.json?limit={str(1000)}&t={date_range}'
        request = requests.get(URL, headers={'User-agent': 'agent'})
    except:
        print('Subreddit not Found')
        return

    request = request.json()
    songs = 0

    # get tracks:
    for post in request['data']['children']:

        if songs < limit:
            title = post['data']['title']

            # clean text
            if '{' in title or '[' in title or '(' in title:
                title = re.sub('[\(\[].*?[\)\]]', "", title)

            if '|' in title:
                title = title.split('|', 1)[0]

            if ' - ' in title and len(title) <= 50:
                name = title.split(' - ')
                song = re.sub('\W+', ' ', name[1])
                artist = re.sub('\W+', ' ', name[0])

                # try to add track to the playlist
                track_ids = sp.search(q='artist:' + artist + ' track:' + song, type='track', limit=1)
                tracks = track_ids['tracks']
                items = tracks['items']

                try:
                    item = items[0]
                    tracks_ids.append(item['id'])
                    songs += 1
                except:
                    print('the song: ' + artist + " - " + song + " was not found on spotify")
                    continue



            else:
                continue



        else:
            break

    sp.user_playlist_add_tracks(username, playlist_id, tracks=tracks_ids)
    print('Playlist Created')
    return

def get_spotify_token(username,client_id,client_secret,redirect_uri):
    # get token

    token = util.prompt_for_user_token(username, scope='playlist-modify-public',
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)
    return token

def create_playlist(name, token, username):

    sp = spotipy.Spotify(auth=token)

    #get all current playlists of a user:
    get_playlists = sp.user_playlists(username)
    playlists = get_playlists['items']

    for n in playlists:
        if n['name'] == name:
            print('playlist already exists')
            return 0

    # create playlist
    endpoint_url = f"https://api.spotify.com/v1/users/{username}/playlists"
    request_body = json.dumps({
        "name": name,
        "public": True
    })
    response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type": "application/json",
                                                                           "Authorization": "Bearer " + token})

    playlist_id = response.json()['id']
    return playlist_id




