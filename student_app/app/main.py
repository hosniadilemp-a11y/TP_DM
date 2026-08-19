import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from student_app.app.database import engine, Base
from student_app.app.api.attempts import router as attempts_router

# Initialize tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Data Mining TP Continuous Evaluation Engine",
    description="Timed True/False Continuous Evaluation Platform for Data Mining TPs",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Router
app.include_router(attempts_router)

# Mount Static directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(PROJECT_ROOT, "static")
os.makedirs(STATIC_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def read_root():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Data Mining Evaluation API Engine is Running. Static files not yet deployed."}

@app.get("/health")
def health_check():
    return {"status": "ok", "app": "TP Continuous Evaluation Engine"}

@app.get("/favicon.ico")
def favicon():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), status_code=204)

@app.get("/.well-known/appspecific/com.chrome.devtools.json")
def chrome_devtools_wellknown():
    return {}
