from fastapi import FastAPI
import dotenv, os

dotenv.load_dotenv()
VERSION = os.getenv("VERSION")
DATE = os.getenv("DATE_RELEASE")

app = FastAPI()

@app.get("/version")
async def get_app():
    return {
        "version": VERSION,
        "date": DATE
    }

