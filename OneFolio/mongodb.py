from decouple import config
import pymongo

mongo_uri = config('MONGO_URI')
client = pymongo.MongoClient(mongo_uri)
db = client["OneFolio"]

users_collection = db["User"]
investments_collection = db["Investment"]