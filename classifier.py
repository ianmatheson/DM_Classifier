import requests
import random
import string
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import numpy as np
import operator
import scipy.stats as ss
from math import pi


#-------------Variables--------------
#we could not make these global if that is better?????
cid = "9d6f6b55c63b442c825236c74f4d8cc5"
secret = "2ee56909011b41e3bc7c25299b9b41cb"
redirect_uri = "https://developer.spotify.com/dashboard/applications/9d6f6b55c63b442c825236c74f4d8cc5"
username = "1278886039" #username id

#All playlist ID's are below
#RAP/Hip-hop
rap1ID = "37i9dQZF1DX0XUsuxWHRQd" #https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd RapCaviar
rap2ID = "4pCLzyVRnWpOivB6RwPREo" #https://open.spotify.com/playlist/4pCLzyVRnWpOivB6RwPREo Rap Playlist 2019
rap3ID = "37i9dQZF1DWUFmyho2wkQU" #https://open.spotify.com/playlist/37i9dQZF1DWUFmyho2wkQU Hip-hop Drive
rap4ID = '5772HGqmp2E99GQo5tfmcJ' #https://open.spotify.com/playlist/5772HGqmp2E99GQo5tfmcJ 90's rap/hip hop
rap5ID = "37i9dQZF1DWT5MrZnPU1zD" #https://open.spotify.com/playlist/37i9dQZF1DWT5MrZnPU1zD Hip hop controller
rap6ID = "5V1TS5zoSk9hNpGeofCAxq" #https://open.spotify.com/playlist/5V1TS5zoSk9hNpGeofCAxq 2016 Rap hits
rap7ID = "2SmIysAFFMz4cBPPaQ70v7" #https://open.spotify.com/playlist/2SmIysAFFMz4cBPPaQ70v7 Hip-hop 2000 classics
rap8ID = "2mlGr2NYuJXRA7M6GYhmNZ" #https://open.spotify.com/playlist/2mlGr2NYuJXRA7M6GYhmNZ Hip-hop Lit
rap9ID = "5iA8wivZWLZ9iCLrvj1PLV" #https://open.spotify.com/playlist/5iA8wivZWLZ9iCLrvj1PLV 90's rap

rapIDs = [rap1ID, rap2ID, rap3ID, rap4ID, rap5ID, rap6ID, rap7ID, rap8ID, rap9ID]

#ROCK
rock1ID = "37i9dQZF1DWXRqgorJj26U" #https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U Rock classics
rock2ID = "37i9dQZF1DX1rVvRgjX59F" #https://open.spotify.com/playlist/37i9dQZF1DX1rVvRgjX59F 90's rock anthems
rock3ID = "5RkXZzyPCKrovrl1XF92vo" #https://open.spotify.com/playlist/5RkXZzyPCKrovrl1XF92vo 70's Rock Classics
rock4ID = "1NIX36ZFWEtgXSbSNghoue" #https://open.spotify.com/playlist/1NIX36ZFWEtgXSbSNghoue Hard Rock Classics
rock5ID = "00VTH4862l4NRuq6F3goLA" #https://open.spotify.com/playlist/00VTH4862l4NRuq6F3goLA Rocks Classics
rock6ID = "41bG5z3KY2eJVGRUTmGnas" #https://open.spotify.com/playlist/41bG5z3KY2eJVGRUTmGnas Best of - Rock Classics
rock7ID = "6LoIIvUyBQBXs7H3gJNT3y" #https://open.spotify.com/playlist/6LoIIvUyBQBXs7H3gJNT3y Rock and roll classics
rock8ID = "4oIIueI3vnEI6RtGuOrwzr" #https://open.spotify.com/playlist/4oIIueI3vnEI6RtGuOrwzr Exam 1
rock9ID = "4282qXajfoO3scbvogeQCW" #https://open.spotify.com/playlist/4282qXajfoO3scbvogeQCW Classics (my playlist)
rock10ID = "2q7gVPXAMNC73Mxqb0LJoC" #https://open.spotify.com/playlist/2q7gVPXAMNC73Mxqb0LJoC Exam 2
rock11ID = "1MfTMvgM5bCsctoUtKwbqy" #https://open.spotify.com/playlist/1MfTMvgM5bCsctoUtKwbqy Exam 3 (all from rock class)
rock12ID = "4lIywN6kXl9KPm3OQ8u8G7" #https://open.spotify.com/playlist/4lIywN6kXl9KPm3OQ8u8G7 Classic rock radio

rockIDs = [rock1ID, rock2ID, rock3ID, rock4ID, rock5ID, rock6ID, rock7ID, rock8ID, rock9ID, rock10ID, rock11ID, rock12ID]

#JAZZ
jazz1ID = "0kpec6BHD5cVFLjYnOqJgL" #https://open.spotify.com/playlist/0kpec6BHD5cVFLjYnOqJgL Bar jazz classics
jazz2ID = "5hZtfYA9YY8kRq5bPPOtQP" #https://open.spotify.com/playlist/5hZtfYA9YY8kRq5bPPOtQP Dixieland classics
jazz3ID = "278sQOsiKoPwJqpvHfjqsV" #https://open.spotify.com/playlist/278sQOsiKoPwJqpvHfjqsV Jazz for dining
jazz4ID = "4KCzwOy4LtlAd0UwCTYOhs" #https://open.spotify.com/playlist/4KCzwOy4LtlAd0UwCTYOhs Jazz Classics
jazz5ID = "5WorvtdlSDEQI8FFx2bB41" #https://open.spotify.com/playlist/5WorvtdlSDEQI8FFx2bB41 Jas (my playlist - check it out)
jazz6ID = "6sU3nSuJzb63Md91cJXs7w" #https://open.spotify.com/playlist/6sU3nSuJzb63Md91cJXs7w Jass
jazz7ID = "37i9dQZF1DX7UE7qrnkvsf" #https://open.spotify.com/playlist/37i9dQZF1DX7UE7qrnkvsf jazz for autumn
jazz8ID = "6UHNDehnrX6zizwRaLHoZE" #https://open.spotify.com/playlist/6UHNDehnrX6zizwRaLHoZE big band and swing jazz
jazz9ID = "05Hd48jdQIz3s8WRrvGnzf" #https://open.spotify.com/playlist/05Hd48jdQIz3s8WRrvGnzf Jazz Playlist

jazzIDs = [jazz1ID, jazz2ID, jazz3ID, jazz4ID, jazz5ID, jazz6ID, jazz7ID, jazz8ID, jazz9ID]

#CLASSICAL

#COUNTRY

#EDM


#----------AUTHORIZATION--------------
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

#-----------INITIALIZATION------------
def mergePlaylists(ids):
    allSongIDs = []
    for id in ids:
        playlist = sp.user_playlist(username, id)
        playlistTracks = (playlist["tracks"])
        playlistSongs = playlistTracks["items"]
        for song in playlistSongs:
            if song['track']['id'] in allSongIDs:
                continue
            else:
                allSongIDs.append(song['track']['id'])

    return allSongIDs

def getFeatures(songIDs):
    #SOMEHOW DEAL WITH FEATURE EXTRACTION AND AVERAGING???
    for id in songIDs:
        features = sp.audio_features(id)
        print(features)



#need different song lists in order to train classifier
rapSongIDs = mergePlaylists(rapIDs)
print("Rap length: ", len(rapSongIDs))
rockSongIDs = mergePlaylists(rockIDs)
print("Rock length: ", len(rockSongIDs))
jazzSongIDs = mergePlaylists(jazzIDs)
print("Jazz length: ", len(jazzSongIDs))


# longestTracks = longestPlay["tracks"]
# longestPlaySongs = longestTracks["items"]

# for song in longestPlaySongs:
#     features = sp.audio_features(song['track']['id'])
#     track = sp.track(song['track']['id'])
#     album = sp.album(track['album']['id'])
#     print(album['genres'])


#-----------DATA CLEANING-------------
# features = sp.audio_features(longestPlaySongs[0]['track']['id'])
# track = sp.track(longestPlaySongs[0]['track']['id'])
# album = sp.album(track['album']['id'])
# print(album['genres'])
# print(track['album'])
# release_date = track['album']['release_date']
# print(release_date)
# print(features)