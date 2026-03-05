import os
import mysql.connector
from services.loggerServices import LogType, Log
from dotenv import load_dotenv

load_dotenv()

class DatabaseService:
    host:str = os.getenv("DATABASE_HOST")
    user:str = os.getenv("DATABASE_USER")
    password:str = os.getenv("DATABASE_PASSWORD")
    database:str = os.getenv("DATABASE_DATABASE")
    
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host= self.host,
                user= self.user,
                password= self.password,
                database= self.database,
            )
            
            self.cursor = self.connection.cursor()
            
            Log(LogType.database, "Berhasil mengakses database")
        except:
            Log(LogType.database, "Gagal mengakses database")
    
    def getConnection(self):
        return self.connection
    
    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()
    
    def closeConnection(self):
        self.connection.close()
        
        
connection:DatabaseService = DatabaseService()