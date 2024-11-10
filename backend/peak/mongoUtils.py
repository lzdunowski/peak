from pymongo.mongo_client import MongoClient
#from pymongo.server_api import ServerApi

def get_db_handle():
    url = "mongodb://admin:admin@mongo:27017/"
    
    client = MongoClient(url)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!\n")
    except Exception as e:
        print(e)
    else:
        return client

def get_collection_handle(db_name, collection_name):
    url = "mongodb://admin:admin@mongo:27017/"
    
    client = MongoClient(url)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!\n")
    except Exception as e:
        print(e)
    else:
        dbname = client[db_name]
        collection = dbname[collection_name]
        return collection
    