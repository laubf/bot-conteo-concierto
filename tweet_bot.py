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

# Fechas de los conciertos
fecha_colombia = date(2025, 5, 21)   # concierto en Colombia
fecha_mexico = date(2025, 10, 14)    # concierto en México

# Fecha de hoy
hoy = date.today()

# Cálculos
dias_desde_colombia = (hoy - fecha_colombia).days
dias_desde_mexico = (hoy - fecha_mexico).days

# Determinar el texto correcto según si ya pasó el concierto de México o no
if hoy < fecha_mexico:
    dias_hasta_mexico = (fecha_mexico - hoy).days
    mensaje = f"{dias_desde_colombia} days since Hozier's concert in Colombia 🇨🇴 🥲 and {dias_hasta_mexico} days until Mexico 🇲🇽"
else:
    mensaje = f"{dias_desde_colombia} days since Hozier's concert in Colombia 🇨🇴 🥲 and {dias_desde_mexico} days since Mexico 🇲🇽 🥹"

# Publicar tweet
response = client.create_tweet(text=mensaje)
print("Tweet publicado:", response)
