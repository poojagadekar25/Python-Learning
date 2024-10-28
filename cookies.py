

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/set-cookie/")
async def set_cookie():
    response = JSONResponse(content={"message": "Cookie set!"})
    response.set_cookie(key="ads_id", value="xyz123")
    return response
