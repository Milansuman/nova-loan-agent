import json
from schema.db import Database

def load_db() -> Database:
    """
    Loads the mock db from the json file
    """
    return json.loads("./app/db/db.json")