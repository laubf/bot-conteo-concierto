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

# Fechas
fecha_concierto_pasado = date(2025, 5, 21)   # concierto ya ocurrido
fecha_concierto_futuro = date(2025, 10, 14)  # próximo concierto

# Fecha de hoy
hoy = date.today()

# Cálculos
dias_desde = (hoy - fecha_concierto_pasado).days
dias_hasta = (fecha_concierto_futuro - hoy).days

# Mensaje
mensaje = f"{dias_desde} days since Hozier's concert 🥲 and {dias_hasta} days until I see him again 🥹"

# Publicar tweet
response = client.create_tweet(text=mensaje)
print("Tweet publicado:", response)

