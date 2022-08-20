

# A file containing the list of possible fields for each collection
NAME_FIELDS = [ "name", "pronunciation", "word formation", "tag", "meaning", "remark" ]


CHARACTER_APPEARANCE = [ "hair", "eyes", "skin", "body type", "cloth", "other" ]
CHARACTER_ABILITIES = [ "taat", "satra", "weapon" ]
CHARACTER_FIELDS = [ "first name", "last name", "age", "gender", "nationality", "occupation", "character appearance", "character ability", "personality" ]


SQUAD_INFO = [ "name", "member count", "specialization" ]
WARRIOR_FIELDS = [ "first name", "last name", "rank", "squad name", ]


LOCATION_FIELDS = [ "name", "region", "significance" ]

# Type = Offense, Defense, Support
SATRA_FIELDS = [ "name", "type", "taat" ]





# Dictionary mapping collection name to field list
COLLECTION_FIELDS_DICT = { "names": NAME_FIELDS, "characters": CHARACTER_FIELDS, 
                            "character appearance": CHARACTER_APPEARANCE, "character ability": CHARACTER_ABILITIES }
