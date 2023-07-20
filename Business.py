from Record import Record


# Omer Kaya


class BusinessLayer:
    def __init__(self, persistence):
        self.persistence = persistence

    def get_records(self):
        return self.persistence.read_db()

    def add_record(self, *args):
        new_record = Record(*args)
        self.persistence.insert_db(new_record)

    def delete_record(self, recordID):
        self.persistence.delete_db(recordID)

    def edit_record(self, recordID, new_values):
        self.persistence.update_db(recordID, new_values)
