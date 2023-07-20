import unittest

from sqlalchemy import create_engine, MetaData, Table

import yaml

with open("../../config.yaml", "r") as yamlfile:
    cfg = yaml.safe_load(yamlfile)

username = cfg["db"]["user"]
password = cfg["db"]["password"]
host = cfg["db"]["host"]
database = cfg["db"]["database"]
table_name = cfg["db"]["table_name"]


class MyTestCase(unittest.TestCase):
    def test_connection(self):
        try:
            self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
            self.connection = self.engine.connect()
            self.metadata = MetaData()
            self.table = Table(table_name, self.metadata, autoload_with=self.engine)

        except:
            self.fail()

        self.defaultTestResult()  # add assertion here


if __name__ == '__main__':
    unittest.main()
