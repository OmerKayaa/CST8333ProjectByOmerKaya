

"""
The Record class is a simple data structure that holds an individual record's data. It contains a single
attribute, columns, which is a tuple of the data values for the record.
"""


class Record:
    def __init__(self, id, REF_DATE, GEO, DGUID, Type_of_product, Type_of_storage, UOM, UOM_ID, SCALAR_FACTOR,
                 SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATE, DECIMALS):
        self.id = id
        self.REF_DATE = REF_DATE
        self.GEO = GEO
        self.DGUID = DGUID
        self.Type_of_product = Type_of_product
        self.Type_of_storage = Type_of_storage
        self.UOM = UOM
        self.UOM_ID = UOM_ID
        self.SCALAR_FACTOR = SCALAR_FACTOR
        self.SCALAR_ID = SCALAR_ID
        self.VECTOR = VECTOR
        self.COORDINATE = COORDINATE
        self.VALUE = VALUE
        self.STATUS = STATUS
        self.SYMBOL = SYMBOL
        self.TERMINATE = TERMINATE
        self.DECIMALS = DECIMALS

    def to_list(self):
        return [self.id, self.REF_DATE, self.GEO, self.DGUID, self.Type_of_product, self.Type_of_storage, self.UOM,
                self.UOM_ID, self.SCALAR_FACTOR, self.SCALAR_ID, self.VECTOR, self.COORDINATE, self.VALUE, self.STATUS,
                self.SYMBOL, self.TERMINATE, self.DECIMALS]

class Record_DTO:
    def __init__(self, REF_DATE, GEO, DGUID, Type_of_product, Type_of_storage, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID,
                 VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATE, DECIMALS):
        self.REF_DATE = REF_DATE
        self.GEO = GEO
        self.DGUID = DGUID
        self.Type_of_product = Type_of_product
        self.Type_of_storage = Type_of_storage
        self.UOM = UOM
        self.UOM_ID = UOM_ID
        self.SCALAR_FACTOR = SCALAR_FACTOR
        self.SCALAR_ID = SCALAR_ID
        self.VECTOR = VECTOR
        self.COORDINATE = COORDINATE
        self.VALUE = VALUE
        self.STATUS = STATUS
        self.SYMBOL = SYMBOL
        self.TERMINATE = TERMINATE
        self.DECIMALS = DECIMALS

    def to_list(self):
        return [self.REF_DATE, self.GEO, self.DGUID, self.Type_of_product, self.Type_of_storage, self.UOM, self.UOM_ID,
                self.SCALAR_FACTOR, self.SCALAR_ID, self.VECTOR, self.COORDINATE, self.VALUE, self.STATUS, self.SYMBOL,
                self.TERMINATE, self.DECIMALS]


# Omer Kaya
