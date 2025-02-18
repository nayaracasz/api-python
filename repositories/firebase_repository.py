import firebase_admin
from firebase_admin import credentials, storage, firestore

class FirebaseRepository:
    def __init__(self):
        cred = credentials.Certificate("firebase_key.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'api-python-70078.firebasestorage.app'
        })
        self.db = firestore.client()
        self.bucket = storage.bucket()

    def uploadFile(self, file_path, destination):
        blob = self.bucket.blob(destination)
        blob.upload_from_filename(file_path)
        blob.make_public()
        return blob.public_url

    def saveUserData(self, userData):
        users_ref = self.db.collection("users")
        users_ref.add(userData)