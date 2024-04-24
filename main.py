import os
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import routes.user_router as user_router

load_dotenv()

app = FastAPI()
app.include_router(user_router.user_router)

@app.get("/")
def read_root():
    return {"Message": "Welcome to Brainwave"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.environ["HOST"],
        reload=bool(os.environ["DEBUG_RELOAD"]),
        port=int(os.environ["PORT"]),
    )
    
