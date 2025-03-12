from database import mongo

class TimeEntry:
    def __init__(self, user_id, check_in, check_out):
        self.user_id = user_id
        self.check_in = check_in
        self.check_out = check_out

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "check_in": self.check_in,
            "check_out": self.check_out
        }

    @staticmethod
    def insert_time_entry(entry):
        return mongo.db.time_entries.insert_one(entry.to_dict())

    @staticmethod
    def get_entries(user_id):
        return list(mongo.db.time_entries.find({"user_id": user_id}, {"_id": 0}))
