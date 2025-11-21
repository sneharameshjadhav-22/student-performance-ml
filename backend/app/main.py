from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.predict_router import router as predict_router
from app.routers.recommend_router import router as recommend_router
from app.routers.xai_router import router as xai_router

app = FastAPI(
    title="Student Performance Prediction API",
    version="1.0.0"
)

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict_router)
app.include_router(recommend_router)
app.include_router(xai_router)

@app.get("/")
def home():
    return {"message": "Backend is running!"}
