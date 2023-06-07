import os
import random
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

app = FastAPI()
total = len(os.listdir('photos'))

@app.get("/")
async def index():
    return {"status": "Working"}

@app.get("/otter")
async def otters( request: Request, photo: int = None):
    if photo is None:
        photo = random.randint(1, total)
    elif photo < 1 or photo > total:
        return {"error": "Invalid photo number."}
    return {
        "photo_number": photo,
        "photo_url": f"{request.base_url}otter/{photo}"
        }

@app.get("/otter/{photo}")
async def otterlink(photo: int):
    if photo is None:
        photo = random.randint(1, total)
    elif photo < 1 or photo > total:
        return {"error": "Invalid photo number."}
    return FileResponse(f'photos/{photo}.png')
        