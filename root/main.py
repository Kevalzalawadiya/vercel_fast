from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'msg': 'welcome home'}

@app.get('/userlist')
async def user_list():
    return {'data': 'user 1'}