import collectionFieldConst
import printing
from bson.json_util import loads
from pymongo import MongoClient
from bson.objectid import ObjectId



def toJSON(col_name):

    record = {}
    col_fields = []

    # Match the collection to its list of fields
    col_fields = collectionFieldConst.COLLECTION_FIELDS_DICT[col_name]
    # if col_name == "names":
    #     col_fields = collectionFieldConst.NAME_FIELDS
    # elif col_name = "character":

    for field in col_fields:

        # If the field is nested
        if field in list(collectionFieldConst.COLLECTION_FIELDS_DICT.keys()):
            nested_record = {}
            for subfield in collectionFieldConst.COLLECTION_FIELDS_DICT[field]:
                user_in = input(subfield + ": ")
                nested_record[subfield] = user_in
            record[field] = nested_record
        else:
            user_in = input(field + ": ")
            record[field] = user_in

    return record


def printAllDatabase(client):
    all_dbs = client.list_database_names()
    i = 1
    while i < len(all_dbs) - 2:
        print(str(i) + ": " + all_dbs[i - 1])
        i += 1


# Print all collections in the current database
def printAllCollections(database):
    print("0: Create a new collection")
    all_cols = database.list_collection_names()
    i = 1
    while i < len(all_cols) + 1:
        print(str(i) + ": " + all_cols[i - 1])
        i += 1
            

def existInList(list, element):
    for i in list:
        if i == element:
            return True
    return False



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
    user_choice = int(input("Connecting collection: "))

    if user_choice == 0:
        working_collection = input("New collection name: ")
    else:
        working_collection = all_cols[user_choice - 1]

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
            insert_count = int(input("How many: "))
            print("Enter record attribute as prompted.")
            if insert_count == 1:
                record = toJSON(working_collection)
                collection.insert_one(record)
            else:
                record_list = []
                while insert_count != 0:
                    record = toJSON(working_collection)
                    record_list.append(record)
                    insert_count -= 1
                collection.insert_many(record_list)


        elif operation == "delete":
            attribute = input("Enter attribute to be deleted by: ")
            input_value = input("Enter " + attribute + ": ")
            query = { attribute: input_value }
            collection.delete_one(query)

        # What to do with nested list?
        # Currently support searching by ONE attribute
        # Find record in CURRENT collection
        elif operation == "find":
            print("\nNAME ATTRIBUTE LIST")
            print(collectionFieldConst.NAME_FIELDS)
            attribute = input("\nSearch by: ")
            while existInList(collectionFieldConst.NAME_FIELDS, attribute) != True:
                print("Attribute doesn't exist. Please select one from the attribute list.")
                attribute = input("Search by: ")
            input_value = input("Enter " + attribute + ": ")
            query = { attribute: input_value }
            records = collection.find(query, {"_id":0})

            # Sort the result
            sort_by = input("Sort by: ")
            sort_type = input("Sort ASC or DESC: ")
            while (sort_type != "ASC" and sort_type != "DESC"):
                sort_type = input("Sort ASC or DESC: ")

            if sort_type == "ASC":
                sort_type = 1
            else:
                sort_type = -1

            records = records.sort(sort_by, sort_type)
            
            print_format = input("Print as TABLE or JSON: ")
            print()
            if (print_format == "JSON"):
                for record in records:
                    print(record)
            else:
                # print(list(records))
                printing.printAsTable(working_collection, list(records))
            print()


        elif operation == "count":
            print("Record count = " + str(collection.count_documents({})))

        elif operation == "print":
            cursor = collection.find({}, {"_id":0})
            for row in cursor:
                print(row)

        # show result in a table format
        elif operation == "printTable":
            cursor = collection.find({}, {"_id":0})
            printing.printAsTable(working_collection, list(cursor))

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
            print("\nExit program. Goodbye.")
            break
        


