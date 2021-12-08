import uvicorn
from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)
