# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://assignment-module12-hans-default-rtdb.firebaseio.com/'
})

# save data
ref = db.reference('py/')
users_ref = ref.child('TV_Shows')
users_ref.set({
    'The Mandalorian': {
        'airdate': 'November 12, 2019',
        'seasons': 2,
        'epsidoe_count': 16
    },
    'The Book of Boba Fett': {
        'airdate': 'December 28, 2021',
        'seasons': 1,
        'episode_count':7
    }
})

# read data
handle = db.reference('py/TV_Shows/The Mandalorian')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())