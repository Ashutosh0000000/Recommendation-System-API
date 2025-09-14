from fastapi import FastAPI
from . import auth, activity, stats

app = FastAPI(title="Recommendation System API", version="1.0.0")

app.include_router(auth.router)
app.include_router(activity.router)
app.include_router(stats.router)

@app.get("/")
def root():
    return {"msg": "Welcome to the Recommendation System API"}

