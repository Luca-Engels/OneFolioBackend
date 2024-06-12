from decouple import config
import pymongo

mongo_uri = config('MONGO_URI')
client = pymongo.MongoClient(mongo_uri)
db = client["OneFolio"]


# TABLE CONTAINS _id | email | password | role | name | address? | accessToken?
users_collection = db["User"]

# TABLE CONTAINS _id | _userId | data 
investments_collection = db["Investment"]
