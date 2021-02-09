import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
import datetime

cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
firebase = firebase.FirebaseApplication(
    'https://bottelegram-3db40-default-rtdb.firebaseio.com/', None)
# print(firebase)


def create():
    today = datetime.datetime.now()
    db.collection('response').document('bagasnabil1').set(
        {
            'name': 'Bagas',
            'creationDate': today,
            'indices': ['NDX', 'OEX', 'S5COND', 'SPX']
        }
    )


collects = db.collections()


for coll in collects:
    print(type(coll))
    for doc in coll.stream():
        print(f'{doc.id} => {doc.to_dict()}')

# create()
