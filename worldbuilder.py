import collectionFieldConst
from bson.json_util import loads
from pymongo import MongoClient
from bson.objectid import ObjectId




def toJSON(col_name):

    record = {}
    col_fields = []

    # Match the collection to its list of fields
    if col_name == "names":
        col_fields = collectionFieldConst.NAME_FIELDS

    for field in col_fields:
        user_in = input(field + ": ")
        record[field] = user_in

    return record


def printAllDatabase(client):
    all_dbs = client.list_database_names()
    i = 1
    while i < len(all_dbs) - 2:
        print(str(i) + ": " + all_dbs[i - 1])
        i+=1


# Print all collections in the current database
def printAllCollections(database):
    all_cols = database.list_collection_names()
    i = 1
    while i < len(all_cols) + 1:
        print(str(i) + ": " + all_cols[i - 1])
        i+=1





if __name__ == "__main__":

    # create a MongoClient to the running mongod instance
    client = MongoClient()
    client = MongoClient('localhost', 27017)

    # Get database and collection that the user wants to work on
    all_dbs = client.list_database_names()
    print("Select a number from the list of existing databases.")
    printAllDatabase(client)
    working_database = all_dbs[int(input("Connecting database: ")) - 1]
    db = client[working_database]
    print("Connected to \"" + working_database + "\"\n")

    all_cols = db.list_collection_names()
    print("Select a number from the list of existing collections in \"" + working_database + "\"")
    printAllCollections(db)
    working_collection = all_cols[int(input("Connecting collection: ")) - 1]
    collection = db[working_collection]
    print("Currently working with \"" + working_collection + "\"\n")

    # Accept user input for operations
    while True:

        operation = input("Operation: ")

        if operation == "showdb":
            printAllDatabase(client)

        elif operation == "showcol":
            printAllCollections(db)

        elif operation == "insert":
            print("Enter record attribute as prompted.")
            record = toJSON(working_collection)
            collection.insert_one(record)

        elif operation == "delete":
            query = input("Enter query in JSON format: ")
            db[working_collection].delete_one(loads(query))

        elif operation == "count":
            print("Record count = " + str(collection.count_documents({})))

        elif operation == "print":
            cursor = collection.find()
            for row in cursor:
                print(row)

        elif operation == "switchdb":
            print("Select a number from the list of existing databases.")
            printAllDatabase(client)
            working_database = all_dbs[int(input("Connecting database: ")) - 1]
            db = client[working_database]
            print("Connected to \"" + working_database + "\"\n")

            all_cols = db.list_collection_names()
            print("Select a number from the list of existing collections in \"" + working_database + "\"")
            printAllCollections(db)
            working_collection = all_cols[int(input("Connecting collection: ")) - 1]
            collection = db[working_collection]
            print("Currently working with \"" + working_collection + "\"\n")

        elif operation == "quit":
            print("Exit program. Goodbye.")
            break
        


