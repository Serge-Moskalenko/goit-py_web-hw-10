from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb+srv://Python_Mongo:1234567890@cluster0.qs4wa.mongodb.net/")
    db = client["hw09"]
    return db