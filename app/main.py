from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AutoDevX", version="1.0.0")

app.include_router(router)

@app.get("/")
async def health():
    return {"status": "AutoDevX Running"}


@app.on_event("startup")
async def startup_event():
    from app.dependencies import startup
    startup()

