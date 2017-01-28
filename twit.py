#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#musisz zainstalowac Tweepy uzywajac pip install tweepy

#Musisz podac swoje dane z rejestracji do API Twittera
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_trump_twitter():
	#z przykladowego kodu tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	all_tweets = []
	#pobieramy po 200 twitow i dopisujemy do listy
	new_tweets = api.user_timeline(screen_name = 'realDonaldTrump',count=200)
	all_tweets.extend(new_tweets)
	#zapisujemy najstarszego twita
	oldest = all_tweets[-1].id - 1
	
	#dopoki dostajemy twity, dopisujemy do listy
	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = 'realDonaldTrump',count=200,max_id=oldest)
		all_tweets.extend(new_tweets)
		#zapisujemy ostatniego pobranego twita
		oldest = all_tweets[-1].id - 1
	
	twitstosave = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.source, tweet.place] for tweet in all_tweets]
	
	with open('twity_trumpa.csv', 'w') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(["id","created_at","text","source","place"])
		writer.writerows(twitstosave)
	pass

if __name__ == '__main__':
	get_trump_twitter()
