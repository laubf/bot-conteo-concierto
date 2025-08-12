from datetime import date
import tweepy
import os

# Fechas
fecha_concierto_pasado = date(2024, 5, 20)   # Fecha de tu concierto pasado
fecha_concierto_nuevo = date(2025, 10, 14)   # Fecha del próximo concierto

hoy = date.today()

# Conteo desde el concierto pasado
dias_desde = (hoy - fecha_concierto_pasado).days

# Conteo hasta el próximo concierto
dias_hasta = (fecha_concierto_nuevo - hoy).days

# Autenticación API v1.1
auth = tweepy.OAuth1UserHandler(
    os.environ['API_KEY'],
    os.environ['API_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET']
)
api = tweepy.API(auth)

# Mensaje combinado
mensaje = f"{dias_desde} days since Hozier's concert 🥲 and {dias_hasta} until I see him again 🥹"

# Publicar tweet
api.update_status(mensaje)
