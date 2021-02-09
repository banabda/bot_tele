import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
import datetime

cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
firebase = firebase.FirebaseApplication('https://bottelegram-3db40-default-rtdb.firebaseio.com/', None)
# print(firebase)
def create():
    today = datetime.datetime.now()
    db.collection('response').document('AMZN').set(
      {
        'name': 'Amazon',
        'creationDate': today,
        'lastClose': 3443.63,
        'indices': [ 'NDX', 'OEX', 'S5COND', 'SPX' ]
      }
    )
docs = db.collection('NYSE')
print(docs.id)

for doc in docs.stream():
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
# for doc in docs:
#     stock = doc.to_dict()
#     print(stock)
# print(db.collection('response'))
# create()