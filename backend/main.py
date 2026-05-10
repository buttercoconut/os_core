"""Main FastAPI application for OS core monitoring."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from .process import router as process_router
from .memory import router as memory_router
from .file_system import router as fs_router

app = FastAPI(title="OS Core API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(process_router, prefix="/process")
app.include_router(memory_router, prefix="/memory")
app.include_router(fs_router, prefix="/fs")

@app.get("/")
async def root():
    return {"message": "OS Core API is running."}
