from pymongo import MongoClient
from appconfig import AppConfig


try:
    config = AppConfig()
    uri = config.get_mongo_uri()

    client = MongoClient(uri)
    database = client["sample_mflix"]

    # Create a collection to insert data
    collection_list = database.list_collections()
    collection_list_name: list = []
    collection_to_create: str = "test_collection"

    for c in collection_list:
        collection_list_name.append(c.get('name'))

    if collection_to_create not in collection_list_name:
        database.create_collection(collection_to_create)
    
    collection = database[collection_to_create]

    document_list = [
        {"Pays" : "France"},
        {"Département" : "Val de Marne"}
    ]
    result = collection.insert_many(documents=document_list)
    print(result.acknowledged)

    
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)