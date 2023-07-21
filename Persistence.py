from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, delete, update
from Record import Record
import yaml

with open("./config.yaml", "r") as yamlfile:
    cfg = yaml.safe_load(yamlfile)

username = cfg["db"]["user"]
password = cfg["db"]["password"]
host = cfg["db"]["host"]
database = cfg["db"]["database"]
table_name = cfg["db"]["table_name"]

"""
The PersistenceLayer class handles reading and writing data from/to the database. It provides methods to 
read data from a database and store them as Record objects, and to write these records back to the database.
"""


class PersistenceLayer:
    def __init__(self):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
        self.connection = self.engine.connect()
        self.metadata = MetaData()
        self.table = Table(table_name, self.metadata, autoload_with=self.engine)
        self.records = []

    # Database reader
    def read_db(self):
        query = select(self.table)
        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        self.records = [Record(*row) for row in ResultSet]
        return ResultSet

    # Database writer (insert)
    def insert_db(self, record):
        # Exclude the id field when inserting a new record
        query = self.table.insert().values(
            {column.name: value for column, value in zip(self.table.columns, record.to_list()) if column.name != 'id'})
        self.connection.execute(query)
        self.connection.commit()

    # Database deleter
    def delete_db(self, id):
        query = delete(self.table).where(self.table.c.id == id)
        self.connection.execute(query)
        self.connection.commit()

    # Database updater
    def update_db(self, id, new_values):
        query = update(self.table).where(self.table.c.id == id).values(new_values)
        self.connection.execute(query)
        self.connection.commit()

