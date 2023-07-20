import unittest

from Persistence import PersistenceLayer
from Record import Record


"""
This is a unit test class for the PersistenceLayer. It tests the read_csv and write_csv methods by checking 
the data read from the CSV file and written to the CSV file.
"""


class TestPersistenceLayer(unittest.TestCase):

    testString = "Test-1"

    def setUp(self):
        # setting up before each test
        print("Setting Up Test\n\n\tOmer Kaya\n")
        self.persistence = PersistenceLayer()
        self.record = Record(9999, '1970-03', 'Canada', None, self.testString, 'Cold and common storage', 'Tonnes', 288, 'units ',
                        0, 'v722342', '1.1.1', 680, None, None, None, 0)

    def test_read_db(self):
        ResultSet = self.persistence.read_db()
        self.records = [Record(*row) for row in ResultSet]
        self.assertTrue(len(self.records) >= 7000)

    def test_insert_db(self):
        print("\n\t---Testing insert---\n")
        self.persistence.insert_db(self.record)
        ResultSet = self.persistence.read_db()
        self.records = [Record(*row) for row in ResultSet]
        # Check if the fields of the last record match the fields of the inserted record
        for r in self.records:
            if r.Type_of_product == self.testString:
                self.defaultTestResult()
                return
        self.fail("Item insertion passed but cannot find in database")

    def test_update_db(self):
        print("\n\t---Testing update---\n")
        id = 7497
        new_values = {'REF_DATE': 'TEST'}  # replace with actual column names and new values
        self.persistence.update_db(id,new_values)
        ResultSet = self.persistence.read_db()
        self.records = [Record(*row) for row in ResultSet]
        for r in self.records:
            if r.REF_DATE == "TEST":
                self.defaultTestResult()
                return
        self.fail("no update found")

    def test_delete_db(self):
        print("\n\t---Testing delete---\n")
        self.persistence.delete_db(7497)  # replace 1 with actual id
        self.persistence.read_db()
        self.assertFalse(any(r.id == 7497 for r in self.persistence.records), "Record not deleted from database")

if __name__ == "__main__":
    unittest.main()

