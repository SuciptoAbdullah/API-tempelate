from models.tableModel import Table

class Users(Table):
    tableName:str = "users"
    primaryKeyColumn:str = "user_id"
    
    def __init__(self):
        super().__init__()