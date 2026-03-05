from fastapi import FastAPI as Api
from services.databaseService import DatabaseService
from models.users import Users

app = Api()

@app.get('/')
def index():
    return {}

@app.get('/users')
def getUser():
    user = Users().leftJoin('role_id', 'roles', 'role_id').select('user_id', 'user_name', 'user_email', 'role_name').get()
    return user

@app.get('/users/byid/{id}')
def getUser(id:int=1):
    user = Users().where('id', '=', id)
    return user.get()