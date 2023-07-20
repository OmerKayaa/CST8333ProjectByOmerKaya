import unittest
from Business import BusinessLayer
from Persistence import PersistenceLayer


# Omer Kaya


"""
This is a unit test class for the BusinessLayer. It tests the add_record, delete_record and edit_record methods 
by manipulating a set of test records and checking that the correct changes are made.
"""


class TestBusinessLayer(unittest.TestCase):

    def setUp(self):
        print("Setting Up Test\n\n\tOmer Kaya\n")
        self.filename = "./test.csv"
        self.persistence = PersistenceLayer(self.filename)
        self.business = BusinessLayer(self.persistence)
        self.persistence.read_csv()

    def test_add_record(self):
        initial_len = len(self.business.records)
        self.business.add_record(*tuple(str(_) for _ in range(16)))
        self.assertEqual(len(self.business.records), initial_len + 1)

    def test_delete_record(self):
        initial_len = len(self.business.records)
        self.business.add_record(*tuple(str(_) for _ in range(16)))
        self.business.delete_record(initial_len)  # delete the record we just added
        self.assertEqual(len(self.business.records), initial_len)

    def test_edit_record(self):
        self.business.add_record(*tuple(str(_) for _ in range(16)))
        initial_record = self.business.records[-1]
        self.business.edit_record(len(self.business.records)-1, 0, "new value")
        updated_record = self.business.records[-1]
        self.assertNotEqual(initial_record, updated_record)
        self.assertEqual(updated_record.columns[0], "new value")

if __name__ == "__main__":
    unittest.main()
