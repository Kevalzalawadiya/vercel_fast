from fastapi import FastAPI
import uvicorn
from project.views import app as router 


app = FastAPI()
app.include_router(router, prefix="/account", tags=["account"])

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)