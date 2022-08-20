# Methods for printing



import collectionFieldConst
import textwrap

def tableHeadingFormat(working_collection):
    all_fields = collectionFieldConst.COLLECTION_FIELDS_DICT[working_collection]

    if working_collection == "names":
        for field in all_fields:
            if field == "meaning":
                print("{:<25}".format(field), end ="")
            elif field == "pronunciation" or field == "word formation":
                print("{:<20}".format(field), end ="")
            else:
                print("{:<15}".format(field), end ="")
        print()

    elif working_collection == "characters":
        for field in all_fields:
            if field == "age":
                print("{:<5}".format(field), end ="")
            elif field == "gender":
                print("{:<15}".format(field), end ="")
            elif field == "character appearance":
                appearance_fields = collectionFieldConst.COLLECTION_FIELDS_DICT[field]
                for subfield in appearance_fields:
                    print("{:<25}".format(subfield), end ="")
            elif field == "character ability":
                ability_fields = collectionFieldConst.COLLECTION_FIELDS_DICT[field]
                for subfield in ability_fields:
                    print("{:<15}".format(subfield), end ="")
            else:
                print("{:<15}".format(field), end ="")
        print()


def namesPrintTable(working_collection, list):

    tableHeadingFormat(working_collection)

    for record in list:
        needWrapping = False
        multirows = []
        for key in record:
            # if record[key] == "":
            #     substitute = "NaN"
            #     print("{:<15}".format(substitute), end = "\t")
            if key == "meaning":
                if len(record[key]) > 25:
                    needWrapping = True
                    multirows = textwrap.wrap(record[key], width=24)
                    print("{:<25}".format(multirows[0]), end = "")
                else:
                    print("{:<25}".format(record[key]), end = "")
            elif key == "pronunciation" or key == "word formation":
                print("{:<20}".format(record[key]), end ="")   
            else:
                print("{:<15}".format(record[key]), end = "")
            
        print()
        if needWrapping == True:
            indent = " "
            index = 1
            while index < len(multirows):
                for i in range(70):
                    print(indent, end = "")
                print(multirows[index])
                index += 1

# What to do if unknown number of solumn needs wrapping?
def charactersPrintTable(working_collection, list):
    tableHeadingFormat(working_collection)

    for record in list:
        needWrapping = False
        multirows = []
        for key in record:
            # if record[key] == "":
            #     substitute = "NaN"
            #     print("{:<15}".format(substitute), end = "\t")
            if key == "skin":
                if len(record[key]) > 25:
                    needWrapping = True
                    multirows = textwrap.wrap(record[key], width=24)
                    print("{:<25}".format(multirows[0]), end = "")
                else:
                    print("{:<25}".format(record[key]), end = "")
            
        print()
        if needWrapping == True:
            indent = " "
            index = 1
            while index < len(multirows):
                for i in range(70):
                    print(indent, end = "")
                print(multirows[index])
                index += 1


def printAsTable(working_collection, list):

    if working_collection == "names":
        namesPrintTable(working_collection, list)
    elif working_collection == "characters":
        charactersPrintTable(working_collection, list)
    
