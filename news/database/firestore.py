# import firebase_admin
# from firebase_admin import credentials

# # cred = credentials.Certificate('news/spiders/manage-work-firebase-adminsdk-845gt-8917e6afde.json')
# cred = credentials.Certificate('manage-work-firebase-adminsdk-845gt-8917e6afde.json')
# default_app = firebase_admin.initialize_app(cred)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('news/database/manage-work-firebase-adminsdk-845gt-8917e6afde.json')
# cred = credentials.Certificate('manage-work-firebase-adminsdk-845gt-8917e6afde.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_data(json, collection):
    doc_ref = db.collection(collection)
    doc_ref.add(json)