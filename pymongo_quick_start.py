from pymongo import MongoClient
from appconfig import AppConfig


config = AppConfig()
uri = config.get_mongo_uri()

# Create a new client and connect to the server
client = MongoClient(uri)


try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    databases = client.list_database_names()
    print(databases)
    database = client.get_database("sample_mflix")

    movies = database.get_collection("movies")
    query = {"title": "Titanic"}
    
    movie = movies.find_one(query)
    print(movie)
    

    client.close()
    
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)

