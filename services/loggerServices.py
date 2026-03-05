class LogType:
    database:str = "Database"
    sqlQuery:str = "SQL Query"

class Log:
    def __init__(self, type:str, massage:str):
        print(f"{type}: {massage}")