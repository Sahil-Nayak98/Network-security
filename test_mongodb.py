
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://nayaksahiljsr_db_user:Sahil798@cluster0.l3lfwvp.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)