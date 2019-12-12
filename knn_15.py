import requests
import random
import string
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import numpy as np
import operator
import scipy.stats as ss
from math import pi
import math
from sklearn.model_selection import train_test_split


def split_data(data):
    #dropping first column since trackID is not needed for classifiers
    data = data.drop('trackID', axis = 1)
    train, test = train_test_split(data, test_size = 0.25, random_state = 21)
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
knnTrainingDict = {'classical': classical_train, 'country': country_train, 'edm': edm_train, 'jazz': jazz_train, 'rap': rap_train, 'rock': rock_train}

#Have to name dfs in order to compare if classifier found correct playlist or not
classical_test.name = 'classical'
country_test.name = 'country'
edm_test.name = 'edm'
jazz_test.name = 'jazz'
rap_test.name = 'rap'
rock_test.name = 'rock'

#compiling all in one list to make looping easier
allPlaylists = ['classical', 'country', 'edm', 'jazz', 'rap', 'rock']

#creating a central dictionary with all features separated by playlists for graphing
features = jazz.columns.values
features = np.delete(features, 0)
featDict = dict.fromkeys(['classical', 'country', 'edm', 'jazz', 'rap', 'rock'], dict.fromkeys([ "acousticness", 
    "danceability", "energy", "instrumentalness", "key", "loudness", 
    'speechiness', "tempo", 'valence'], []))


#-------KNN ALGORITHM AND HELPERS-------
def euclideanDistance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square((data1[x] - data2[x]))
    return np.sqrt(distance)

#used to loop through all items and call euclideanDist on each one
def distances(trainingSet, testSong):
    distanceDict = {}
    length = testSong.shape[0]
    for genre, features in trainingSet.items():
        dist = [[euclideanDistance(features.iloc[x], testSong, length), genre] for x in range(len(features))]
        distanceDict[genre] = dist
    return distanceDict

#finding k nearest neighbor with keys and names
def knn(sortedDistances, k):
    counter={}
    for key in sortedDistances.keys():
        counter[key] = 0  
    neighborKeyName=[]
    for i in range(k):
        minValue=10000
        for key, value in sortedDistances.items():
            if value[0][0]<minValue:
                minName=value[0][1]
                minKey=key
                minValue = value[0][0]
        del(sortedDistances[minKey][0])
        counter[minKey]=counter[minKey]+1
        neighborKeyName.append([minKey, minName])
    return counter, neighborKeyName

knnsmallTrain = {'classical': classical_train.head(5), 'jazz': jazz_train.head(5)}
#initializing counters for correctness
sumCorrect = 0
sumTotal = 0
#looping thrugh all playlist lists
for df in testingDFs:
	correct = 0
	total = 0
	for i in range(len(df)):
		distList = distances(knnTrainingDict, df.iloc[i])
		sortedDict={}
		#looping thorugh distList
		for key in distList.keys():
		    sortedDict[key]=sorted(distList[key], key=operator.itemgetter(0))
		counter, neighborKeyAndId = knn(sortedDict, 15)
		#finding prediction
		prediction=max(counter.items(), key=operator.itemgetter(1))[0]
		#if prediction is correct, increase correct
		if(prediction == df.name):
			sumCorrect += 1
			correct += 1
		sumTotal += 1
		total += 1
	print("KNN:", df.name, "fraction correct: ",float(correct/total))

print("KNN - Total fraction correct: ",float(sumCorrect/sumTotal))
print("-------------------")

