import sys
import re
import praw
import spotipy
import spotipy.util as util
import json
import requests


def reddit_tracks(range,limit):
    # log in
    reddit = praw.Reddit(client_id='Fm0qAH9996SISGzCdMJvhw',
                         client_secret='xCWRH52_3WhT6tlYPqatT64tm8ganQ',
                         user_agent='agent')

    # get top songs from reddit:
    hot_posts = reddit.subreddit('Metal').top(range, limit=100)
    songs = {}
    for post in hot_posts:
        if len(songs)<limit:
            title = post.title
            if '{' in post.title or '[' in post.title or '(' in post.title:
                title = re.sub('[\(\[].*?[\)\]]', "", title)

            if ' - ' in title and len(title) <= 50:
                name = title.split('-')
                song = re.sub('[^A-Za-z0-9]+', ' ',name[1])
                artist = re.sub('[^A-Za-z0-9]+', ' ',  name[0])

                # add artist and song to dict
                songs[artist] = song
        else:
            break

    return songs

def get_spotify_token(username):
    # get token

    token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public',
                                       client_id='1610ed9ebbbc4becada9451b3b3c73f2',
                                       client_secret='ab8c18e4221f4f41b45acaf9f4311ed7',
                                       redirect_uri='http://localhost:8888/callback')
    return token

def select_playlist(name,public,token,username):

    sp = spotipy.Spotify(auth=token)

    #get all current playlists of a user:
    get_playlists = sp.user_playlists(username)
    playlists = get_playlists['items']

    for n in playlists:
        if n['name'] == name:
            print('playlist already exists')
            sys.exit()

    # create playlist
    endpoint_url = f"https://api.spotify.com/v1/users/exploderx95/playlists"
    request_body = json.dumps({
        "name": name,
        "public": public
    })
    response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type": "application/json",
                                                                           "Authorization": "Bearer " + token})

    playlist_id = response.json()['id']
    return playlist_id

def add_tracks(playlist_id,songs):
    sp = spotipy.Spotify(auth=token)
    tracks_ids = []

    for i in songs:
        track_ids = sp.search(q='artist:' + i + ' track:' + songs[i], type='track', limit=1)
        tracks = track_ids['tracks']
        items = tracks['items']
        try:
            item = items[0]
            tracks_ids.append(item['id'])
        except:
            print('the song: ' + i + ": " + songs[i] + "was not found in spotify")

    sp.user_playlist_add_tracks(username, playlist_id, tracks=tracks_ids)
    print('Playlist Created')




if __name__ ==  '__main__':
    username = 'exploderx95'
    songs = reddit_tracks('year',15)
    token = get_spotify_token(username)
    playlist_id = select_playlist('best_yearly',True,token,username)
    add_tracks(playlist_id,songs)

