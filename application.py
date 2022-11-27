from poemlib.poemgen import poemgen
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Do you ready to get today's poem? Call /poem"
    }


@app.get("/poem/")
async def poem():
    poem = poemgen()
    return poem


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")