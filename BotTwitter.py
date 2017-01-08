#!/home/code/Escritorio
# -*- coding: utf-8 -*-

##################################################################

	
import tweepy

# Proceso de autentificacion con OAuth

consumer_key="xxxxxxxxxxxxxxxxxx"
consumer_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)
# Para retweetear un tweet
idtweet = 815349037343703044
#API.retweet(idtweet)
# Para enviar unos tweets

status = "Hello world!"
#API.update_status(status)
status = "Tweepy es una librería que se usa para enviar tweets"
#API.update_status(status)

status = "Tweet enviado desde la API de Twitter, accediendo desde Python"
#API.update_status(status)
status = "Lo conseguí! https://www.youtube.com/watch?v=aOl4oeHZnBk"
#API.update_status(status)


#Para mandar un mensaje directo
text = "Este mensaje no es directo"
#API.send_direct_message(id, text)



text = "te estoy enviando esto desde la API, Lo he conseguido"
#API.send_direct_message(id, text)







