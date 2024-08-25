import json

class Database:
    @staticmethod
    def save(data):
        with open("scraped_data.json", "w") as f:
            json.dump(data, f, indent=4)

