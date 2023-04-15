import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Test": "App"}

if __name__ == '__main__':
    uvicorn.run(app)