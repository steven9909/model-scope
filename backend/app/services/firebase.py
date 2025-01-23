import firebase_admin as admin
import firebase_admin.firestore as firestore


class FirebaseApp:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FirebaseApp, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        admin.initialize_app()  # TODO: Setup credentials


class Firestore:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Firestore, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def client() -> firestore.firestore.Client:
        return firestore.client(app=FirebaseApp())
