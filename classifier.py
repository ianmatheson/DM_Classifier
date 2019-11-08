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
# export SPOTIPY_CLIENT_ID='9d6f6b55c63b442c825236c74f4d8cc5'
# export SPOTIPY_CLIENT_SECRET='2ee56909011b41e3bc7c25299b9b41cb'
# export SPOTIPY_REDIRECT_URI='https://developer.spotify.com/dashboard/applications/9d6f6b55c63b442c825236c74f4d8cc5'
cid = "9d6f6b55c63b442c825236c74f4d8cc5"
secret = "2ee56909011b41e3bc7c25299b9b41cb"
redirect_uri = "https://developer.spotify.com/dashboard/applications/9d6f6b55c63b442c825236c74f4d8cc5"
username = "1278886039" #username id
#All playlist ID's are below
#Longest Playlist ever
longestPlayID = "5fMCrRnSy4TauAmM36zrIP" #https://open.spotify.com/playlist/5fMCrRnSy4TauAmM36zrIP
#Biggest Playlist ever
biggestPlayID = "7htu5ftbLBRFAwiuHVcUAg" #https://open.spotify.com/playlist/7htu5ftbLBRFAwiuHVcUAg
#50's party
fiftyPartyID = "7xADHS7Ryc6oMdqBVhNVQ9" #https://open.spotify.com/playlist/7xADHS7Ryc6oMdqBVhNVQ9
#All out 50's
allOutID = "37i9dQZF1DWSV3Tk4GO2fq" #https://open.spotify.com/playlist/37i9dQZF1DWSV3Tk4GO2fq
#100 best songs 50's
bestSongsID = "1al1RStuL4X1erEp935x6c" #https://open.spotify.com/playlist/1al1RStuL4X1erEp935x6c



#----------AUTHORIZATION--------------
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)