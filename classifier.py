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
import math


#-------------Variables--------------
#we could not make these global if that is better?????
cid = "9d6f6b55c63b442c825236c74f4d8cc5"
secret = "2ee56909011b41e3bc7c25299b9b41cb"
redirect_uri = "https://developer.spotify.com/dashboard/applications/9d6f6b55c63b442c825236c74f4d8cc5"
username = "1278886039" #username id


#----------PLAYLIST IDS AND LINKS IN CASE OF INQUIRY...UGLY BUT THOUGHT IT WAS ESSENTIAL-----------
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
rap10ID = "5vgukxj086jbI0VRXIemTQ" #https://open.spotify.com/playlist/5vgukxj086jbI0VRXIemTQ mauras wrap

rapIDs = [rap1ID, rap2ID, rap3ID, rap4ID, rap5ID, rap6ID, rap7ID, rap8ID, rap9ID, rap10ID]

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
rock13ID = "00o5lm5x6yP9rIJIx6qjrJ" #https://open.spotify.com/playlist/00o5lm5x6yP9rIJIx6qjrJ More alt rock and current
rock14ID = "01BCSQLJo2krgnu0OZhG0L" #https://open.spotify.com/playlist/01BCSQLJo2krgnu0OZhG0L Rock n roll classics

rockIDs = [rock1ID, rock2ID, rock3ID, rock4ID, rock5ID, rock6ID, rock7ID, rock8ID, rock9ID, rock10ID, rock11ID, rock12ID, rock13ID, rock14ID]

#JAZZ
# jazz1ID = "0kpec6BHD5cVFLjYnOqJgL" #https://open.spotify.com/playlist/0kpec6BHD5cVFLjYnOqJgL Bar jazz classics
jazz2ID = "5hZtfYA9YY8kRq5bPPOtQP" #https://open.spotify.com/playlist/5hZtfYA9YY8kRq5bPPOtQP Dixieland classics
# jazz3ID = "278sQOsiKoPwJqpvHfjqsV" #https://open.spotify.com/playlist/278sQOsiKoPwJqpvHfjqsV Jazz for dining
jazz4ID = "4KCzwOy4LtlAd0UwCTYOhs" #https://open.spotify.com/playlist/4KCzwOy4LtlAd0UwCTYOhs Jazz Classics
jazz5ID = "5WorvtdlSDEQI8FFx2bB41" #https://open.spotify.com/playlist/5WorvtdlSDEQI8FFx2bB41 Jas (my playlist - check it out)
# jazz6ID = "6sU3nSuJzb63Md91cJXs7w" #https://open.spotify.com/playlist/6sU3nSuJzb63Md91cJXs7w Jass
# jazz7ID = "37i9dQZF1DX7UE7qrnkvsf" #https://open.spotify.com/playlist/37i9dQZF1DX7UE7qrnkvsf jazz for autumn
jazz8ID = "6UHNDehnrX6zizwRaLHoZE" #https://open.spotify.com/playlist/6UHNDehnrX6zizwRaLHoZE big band and swing jazz
jazz9ID = "05Hd48jdQIz3s8WRrvGnzf" #https://open.spotify.com/playlist/05Hd48jdQIz3s8WRrvGnzf Jazz Playlist
# jazz10ID = "478wi4LZyjCS1Jo6y26xnI" #https://open.spotify.com/playlist/478wi4LZyjCS1Jo6y26xnI
jazz11ID = "7A36aaHgeJ3TXlCsVr86CX" #https://open.spotify.com/playlist/7A36aaHgeJ3TXlCsVr86CX GIANT GUY - may delete and redo

jazzIDs = [jazz2ID, jazz4ID, jazz5ID, jazz8ID, jazz9ID, jazz11ID]

#CLASSICAL
classical1ID = "5tXCRZAUKp2uqtmJZNkQxY" #https://open.spotify.com/playlist/5tXCRZAUKp2uqtmJZNkQxY classical
classical2ID = "3fNcrDFpar3QMWAc5fji9G" #https://open.spotify.com/playlist/3fNcrDFpar3QMWAc5fji9G "     "
classical3ID = "0UNHDTybzvJrHmFASPnVgj" #https://open.spotify.com/playlist/0UNHDTybzvJrHmFASPnVgj "     "
classical4ID = "7vbMPSU3IVLBQSDgucTUMP" #https://open.spotify.com/playlist/7vbMPSU3IVLBQSDgucTUMP "     "
classical5ID = "37i9dQZF1DWWEJlAGA9gs0" #https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0 "     "
classical6ID = "1pcKs0Rig9FiVPrj87Iffv" #https://open.spotify.com/playlist/1pcKs0Rig9FiVPrj87Iffv classical essentials
classical7ID = "2Ea3nBAL68c1JQqMC4PMar" #https://open.spotify.com/playlist/2Ea3nBAL68c1JQqMC4PMar classical essentials
classical8ID = "1lS6K85kThX7lkPjJ23daR" #https://open.spotify.com/playlist/1lS6K85kThX7lkPjJ23daR my classical essentials
classical9ID = "1aeZv1CYwR39C6lf2mK1Bj" #https://open.spotify.com/playlist/1aeZv1CYwR39C6lf2mK1Bj
classicalIDs = [classical1ID, classical2ID, classical3ID, classical4ID, classical5ID, classical6ID, classical7ID, classical8ID, classical9ID]

#COUNTRY
country1ID = '4v4zEO7FPn9lKt7pLHao5X' # The only country playlist that matters https://open.spotify.com/playlist/4v4zEO7FPn9lKt7pLHao5X 
country2ID = "2rlCIi7oKEyKTN42BUdMSB" #https://open.spotify.com/playlist/2rlCIi7oKEyKTN42BUdMSB maura Country
country3ID = "5SvjmWVcoJkac9BKud2M6W" #https://open.spotify.com/playlist/5SvjmWVcoJkac9BKud2M6W country
country4ID = "5AOSddZQa4C9bt4E7luY1L" #https://open.spotify.com/playlist/5AOSddZQa4C9bt4E7luY1L Country
country5ID = "48OHCGqtPpbOZLFpN35Xsp" #https://open.spotify.com/playlist/48OHCGqtPpbOZLFpN35Xsp Top country 2013-2019
country6ID = "6o78UWoUeQLks9G785NLsf" #https://open.spotify.com/playlist/6o78UWoUeQLks9G785NLsf
country7ID = "13HYHjm9Tv5QWJIFSQlv7h" #https://open.spotify.com/playlist/13HYHjm9Tv5QWJIFSQlv7h Country Classics
country8ID = "7fOzCZJTRCmvZ0G3Zy4AVW" #https://open.spotify.com/playlist/7fOzCZJTRCmvZ0G3Zy4AVW Country new and old
country9ID = "0t6GshCAD6ym2ZWz7rjzoZ" #https://open.spotify.com/playlist/0t6GshCAD6ym2ZWz7rjzoZ country playlist

countryIDs = [country1ID, country2ID, country3ID, country4ID, country5ID, country6ID, country7ID, country8ID, country9ID]

#EDM
edm1ID = "0tEj701zR0xgOXhXucX57B" #https://open.spotify.com/playlist/0tEj701zR0xgOXhXucX57B maura edm (abg)
edm2ID = "4xXt0NNILAMwXsXjkdIaAK" #https://open.spotify.com/playlist/4xXt0NNILAMwXsXjkdIaAK mike edm
edm3ID = "4ykwAEFulaKPDQpflIr0k7" #https://open.spotify.com/playlist/4ykwAEFulaKPDQpflIr0k7 electric vibes?
edm4ID = "5mhb5QRMXgufiqEuHL74gi" #https://open.spotify.com/playlist/5mhb5QRMXgufiqEuHL74gi
edm5ID = "5P1PcTioNlUzkW0bdr5FSg" #https://open.spotify.com/playlist/5P1PcTioNlUzkW0bdr5FSg edm classics
edm6ID = "0rA7eold66Wk05o4irdrqq" #https://open.spotify.com/playlist/0rA7eold66Wk05o4irdrqq chill edm
edm7ID = "3Di88mvYplBtkDBIzGLiiM" #https://open.spotify.com/playlist/3Di88mvYplBtkDBIzGLiiM edm classics 2019
edm8ID = "2dL2ewiigZs9LuJHwBH2J0" #https://open.spotify.com/playlist/2dL2ewiigZs9LuJHwBH2J0
edm9ID = "2R3Fh6q5rlpMbRU8oeRT1p" #https://open.spotify.com/playlist/2R3Fh6q5rlpMbRU8oeRT1p Insane (but more chill edm)
edm10ID = "0sJLDKZxFWlcQFIIT45iQE" #https://open.spotify.com/playlist/0sJLDKZxFWlcQFIIT45iQE edm music
edm11ID = "2W32HNDe5OgNsPvciLm1Ix" #https://open.spotify.com/playlist/2W32HNDe5OgNsPvciLm1Ix best edm music of all time
edm12ID = "5Yn8cufVoLX4QubVGUOj9n" #https://open.spotify.com/playlist/5Yn8cufVoLX4QubVGUOj9n house music

edmIDs = [edm1ID, edm2ID, edm3ID, edm4ID, edm5ID, edm6ID, edm7ID, edm8ID, edm9ID, edm10ID, edm11ID, edm12ID]

#------------IDS DONE-----------------


#----------AUTHORIZATION--------------
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)


def handlePlaylists():
    #-----------DATA HANDLING------------
    def mergePlaylists(ids):
        allSongIDs = []
        for id in ids:
            playlist = get_playlist_tracks(id)
            for song in playlist:
                if song['track']['id'] in allSongIDs:
                    continue
                allSongIDs.append(song['track']['id'])
        return allSongIDs

    def get_playlist_tracks(playlist_id):
        results = sp.user_playlist_tracks(username,playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks

    def getFeatures(songIDs):
        #SOMEHOW DEAL WITH FEATURE EXTRACTION AND AVERAGING???
        for id in songIDs:
            features = sp.audio_features(id)
            print(features)

    #PRINTING OUT LENGTH OF ALL GENRES MERGED PLAYLISTS WITHOUT DUPLICATES
    rapSongIDs = mergePlaylists(rapIDs)
    print("Rap length: ", len(rapSongIDs))
    rockSongIDs = mergePlaylists(rockIDs)
    print("Rock length: ", len(rockSongIDs))
    jazzSongIDs = mergePlaylists(jazzIDs)
    print("Jazz length: ", len(jazzSongIDs))
    classicalSongIDs = mergePlaylists(classicalIDs)
    print("Classical length: ", len(classicalSongIDs))
    countrySongIDs = mergePlaylists(countryIDs)
    print("Country length: ", len(countrySongIDs))
    edmSongIDs = mergePlaylists(edmIDs)
    print("EDM length: ", len(edmSongIDs))


def feature_extraction():
    songLists = [rapSongIDs, rockSongIDs, jazzSongIDs, classicalSongIDs, countrySongIDs, edmSongIDs]
    rap_features, rap_ids, rock_features, rock_ids, jazz_features, jazz_ids, country_features, country_ids, edm_features, edm_ids = [],[],[],[],[],[],[],[],[],[] 
    for song in rapSongIDs:#done
        audio_features = sp.audio_features(song)
        #print(audio_features[0])
        if audio_features[0]!=None:
            rap_ids.append(song)
            rap_features.append(audio_features[0])

    for song in rockSongIDs:#done
        audio_features = sp.audio_features(song)
        #print(audio_features[0])
        if audio_features[0]!=None:
            rock_ids.append(song)
            rock_features.append(audio_features[0])


    for song in jazzSongIDs:#done
        audio_features = sp.audio_features(song)
        #print(audio_features[0])
        if audio_features[0]!=None:
            jazz_ids.append(song)
            jazz_features.append(audio_features[0])

    for song in classicalSongIDs: #done
        try:
            audio_features = sp.audio_features(song)
            if audio_features[0]!=None:
                classical_ids.append(song)
                classical_features.append(audio_features[0])
        except Exception:
            continue

    for song in countrySongIDs:
        try:
            audio_features = sp.audio_features(song)
            #print(audio_features[0])
            if audio_features[0]!=None:
                country_ids.append(song)
                country_features.append(audio_features[0])
        except Exception:
            continue

    for song in edmSongIDs:
        try:
            audio_features = sp.audio_features(song)
            #print(audio_features[0])
            if audio_features[0]!=None:
                edm_ids.append(song)
                edm_features.append(audio_features[0])
        except Exception:
            continue

    rap_df = pd.DataFrame(rap_features, index = rap_ids)
    rock_df = pd.DataFrame(rock_features, index = rock_ids)
    jazz_df = pd.DataFrame(jazz_features, index = jazz_ids)
    classical_df = pd.DataFrame(classical_features, index = classical_ids)
    country_df = pd.DataFrame(country_features, index = country_ids)
    edm_df = pd.DataFrame(edm_features, index = edm_ids)


    rap_df = rap_df.drop(["uri", "track_href", "analysis_url", "type", "id", "mode", "duration_ms", "liveness", "time_signature"], axis = 1)
    rock_df = rock_df.drop(["uri", "track_href", "analysis_url", "type", "id", "mode", "duration_ms", "liveness", "time_signature"], axis = 1)
    jazz_df = jazz_df.drop(["uri", "track_href", "analysis_url", "type", "id", "mode", "duration_ms", "liveness", "time_signature"], axis = 1)
    classical_df = classical_df.drop(["uri", "track_href", "analysis_url", "type", "id", "mode", "duration_ms", "liveness", "time_signature"], axis = 1)
    country_df = country_df.drop(["uri", "track_href", "analysis_url", "type", "id", "mode", "duration_ms", "liveness", "time_signature"], axis = 1)
    edm_df = edm_df.drop(["uri", "track_href", "analysis_url", "type", "id", "mode", "duration_ms", "liveness", "time_signature"], axis = 1)


    rap_df.to_csv("rap_csv.csv")
    rock_df.to_csv("rock_csv.csv")
    jazz_df.to_csv("jazz_csv.csv")
    classical_df.to_csv("classical_csv.csv")
    country_df.to_csv("country_csv.csv")
    edm_df.to_csv("edm_csv.csv")



#split data into test and training sets
def split_data(data):
    full = data
    test = []
    test = pd.DataFrame(data.sample((math.floor(len(data)*0.25))))
    train = data[~data.isin(test)].dropna()
    test = test.reset_index()
    return train,test

#READING IN DATA
def read_data():
    classical = pd.read_csv('data/classical_csv.csv')
    country = pd.read_csv('data/country_csv.csv')
    edm = pd.read_csv('data/edm_csv.csv')
    jazz = pd.read_csv('data/jazz_csv.csv')
    rap = pd.read_csv('data/rap_csv.csv')
    rock = pd.read_csv('data/rock_csv.csv')
    #Renaming the first column to trackID
    classical = classical.rename(columns={'Unnamed: 0': 'trackID'})
    country = country.rename(columns={'Unnamed: 0': 'trackID'})
    edm = edm.rename(columns={'Unnamed: 0': 'trackID'})
    jazz = jazz.rename(columns={'Unnamed: 0': 'trackID'})
    rap = rap.rename(columns={'Unnamed: 0': 'trackID'})
    rock = rock.rename(columns={'Unnamed: 0': 'trackID'})
    return classical, country, edm, jazz, rap, rock


# -------- VARIABLES NEEDED ------------
#calling read data function
classical, country, edm, jazz, rap, rock = read_data()
#splitting all the data needed
classical_train,classical_test = split_data(classical)
country_train,country_test = split_data(country)
edm_train,edm_test = split_data(edm)  
jazz_train,jazz_test = split_data(jazz)
rap_train,rap_test = split_data(rap)
rock_train,rock_test = split_data(rock)

#combining all lists into one large list for training and testing
trainingDFs = [classical_train, country_train, edm_train, jazz_train, rap_train, rock_train]
testingDFs = [classical_test, country_test, edm_test, jazz_test, rap_test, rock_test]


featDict = dict.fromkeys(['classical', 'jazz', 'rap', 'rock'], dict.fromkeys(['trackID', 
	"acousticness", "danceability", "energy", "instrumentalness", "key", "loudness", 
    'speechiness', "tempo", 'valence'], []))




# -------- NAIVE BAYES ---------
# https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/







#-----------DATA CLEANING-------------
# features = sp.audio_features(longestPlaySongs[0]['track']['id'])
# track = sp.track(longestPlaySongs[0]['track']['id'])
# album = sp.album(track['album']['id'])
# print(album['genres'])
# print(track['album'])
# release_date = track['album']['release_date'] IMPORTANT DONT DELETE
# print(release_date)
# print(features)