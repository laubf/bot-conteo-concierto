import os
import tweepy
from datetime import date

# Autenticación con API v2
client = tweepy.Client(
    bearer_token=os.environ['BEARER_TOKEN'],
    consumer_key=os.environ['API_KEY'],
    consumer_secret=os.environ['API_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)

# Fecha del concierto
fecha_concierto = date(2025, 5, 21)
hoy = date.today()
dias_transcurridos = (hoy - fecha_concierto).days

# Crea el mensaje
mensaje = f"{dias_transcurridos} days since Hozier's concert 🥲"

# Publica el tweet
response = client.create_tweet(text=mensaje)
print("Tweet publicado:", response)
