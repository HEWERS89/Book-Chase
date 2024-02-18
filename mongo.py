import os 
import pymongo
if os.path.exists("env.py"):
 import env

 MONGO_URI = os.environ.get("MONGO_URI")
 DATABASE ="Bookcase01"
 COLLECTION="user"

 def monog_connect(url):
  try:
   conn = pymongo.MongoClient(url)
   print("Connected to MongoDB successfully!!!")
   return conn
  except pymongo.errors.ConnectionFailure as e:
   print("Could not connect to MongoDB : %s") % e

   conn = monog_connect(MONGO_URI)

   coll=conn[DATABASE][COLLECTION]

   documents = coll.find()

   for doc in documents:
    print(doc) 