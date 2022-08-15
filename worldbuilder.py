from pymongo import MongoClient
from bson.objectid import ObjectId

# create a MongoClient to the running mongod instance
client = MongoClient()
client = MongoClient('localhost', 27017)

# A single instance of MongoDB can support multiple independent databases.
# Create a database called "Eshasanti". mydatabase now refers to Eshasanti database
# Automatically created if no database of the name exists.
eshasanti_db = client['Eshasanti']

# Create a collection called "names", which 
names_col = eshasanti_db['names']

# Get input from user
name_in = input("Name: ")
pronunciation_in = input("Pronunciation: ")
meaning_in = input("Meaning: ")
word_formation_in = input("Wordformation: ")
remark_in = input("Remark: ")
tag_in = input("Tag: ")
# print("Result")
# print("Name\t" + name_in)
# print("Pronunciation\t" + pronunciation_in)
# print("Meaning\t" + meaning_in)
# print("Word formation\t" + word_formation_in)
# print("Remark\t" + remark_in)
# print("Tag: " + tag_in)

# Create a JSON record from the user input
record = {
    "name": name_in,
    "pronunciation": pronunciation_in,
    "meaning": meaning_in,
    "wordFormation": word_formation_in,
    "remark": remark_in,
    "tag": tag_in
}

print(record)

# Insert the JSON record into the collection
#id = names_col.insert_one(record)

print("Record count = " + str(names_col.count_documents({})))
cursor = names_col.find()
for row in cursor:
    print(row)


