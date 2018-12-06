import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

cred = credentials.Certificate('./secret.json')
default_app = firebase_admin.initialize_app(cred, {
  'storageBucket': 'computacionfisica-49742.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()

BASE_PHOTOS = './webcam/{photo_name}.jpg'
def photo_path(photo_name):
  return BASE_PHOTOS.format(photo_name=photo_name)

import subprocess as sp
import datetime as dt

# Obteniendo la fecha actual para nombrar a la foto tomada
now = dt.datetime.now()
str_date = now.strftime("%Y-%m-%d[%H:%M:%S]")

# Configuración de las llamadas a la consola
shell_calls = [
  './takephotos.sh',
  str_date
]

# Llamando a los procesos
sp.call(shell_calls)

# Subiendo las imágenes a Storage
new_photo_blob = bucket.blob(str_date)
new_photo_blob.upload_from_filename(filename=photo_path(str_date))


# Guardando el registo de la foto

photo_meta = {
  'photoName': str_date,
  'takeTime': now
}

db.collection('photos').add(photo_meta)