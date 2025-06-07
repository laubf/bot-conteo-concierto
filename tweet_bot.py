import tweepy
import os
from datetime import datetime

# Autenticación con Twitter
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Fecha del concierto
fecha_concierto = datetime(2025, 5, 21)
hoy = datetime.now()
dias = (hoy - fecha_concierto).days

# Tweet
mensaje = f"{dias} since Hozier's concert 🥲"
api.update_status(mensaje)
