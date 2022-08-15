import json
from pymongo import MongoClient
from bson.objectid import ObjectId


NAME_FIELDS = [ "name", "pronunciation", "meaning", "word formation", "tag", "remark" ]




def toJSON(col_name):

    record = {}
    col_fields = []

    # Match the collection to its list of fields
    if col_name == "names":
        col_fields = NAME_FIELDS

    for field in col_fields:
        user_in = input(field + ": ")
        record[field] = user_in

    return record



if __name__ == "__main__":

    # create a MongoClient to the running mongod instance
    client = MongoClient()
    client = MongoClient('localhost', 27017)

    all_dbs = client.list_database_names()
    print("All databases")
    print(all_dbs)
    working_database = input("Connecting database: ")
    db = client[working_database]

    all_cols = db.list_collection_names()
    print("All collections")
    print(all_cols)
    working_collection = input("Working collection: ")
    collection = db[working_collection]

    while True:

        operation = input("Operation: ")

        if operation == "insert":
            print("Enter record attribute as prompted.")
            record = toJSON(working_collection)
            collection.insert_one(record)

        # Doesn't work
        elif operation == "delete":
            query = input("Enter query in JSON format: ")
            db[collection].delete_one(json.loads(query))

        elif operation == "count":
            print("Record count = " + str(collection.count_documents({})))

        elif operation == "print":
            cursor = collection.find()
            for row in cursor:
                print(row)

        elif operation == "switchdb":
            working_database = input("Connecting database: ")
            db = client[working_database]

            working_collection = input("Working collection: ")
            collection = db[working_collection]

        elif operation == "quit":
            print("Exit program. Goodbye.")
            break
        

