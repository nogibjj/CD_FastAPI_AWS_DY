from poemlib.poemgen import poemgen
from get_topic import get_topic
from fastapi import FastAPI
import uvicorn
from enum import Enum


class category(str, Enum):
    all = "all"
    emotion = "shuqing"
    season = "siji"
    landscape = "shanshui"
    weather = "tianqi"
    people = "renwu"
    life = "rensheng"
    dailylife = "shenghuo"
    festival = "jieri"
    animal = "dongwu"
    food = "shiwu"
    plant = "zhiwu"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Do you ready to get today's poem? Call /poem"}


@app.get("/poem/")
async def todaypoem():
    poem = poemgen()
    return poem


@app.get("/poem/{category}")
async def get_poem_topic(poem_type: category):
    """Get an poem type according to the user's input"""
    poem_t = poem_type.value
    poem = get_topic(poem_topic = poem_t)
    return poem


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
