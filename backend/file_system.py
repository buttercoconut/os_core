"""File system module with basic CRUD operations."""

from fastapi import APIRouter, HTTPException
from typing import Dict

router = APIRouter()

# In-memory file system: path -> content
file_system: Dict[str, str] = {}

@router.post("/create")
async def create_file(path: str, content: str = ""):
    if path in file_system:
        raise HTTPException(status_code=400, detail="File already exists")
    file_system[path] = content
    return {"path": path, "content": content}

@router.get("/read")
async def read_file(path: str):
    if path not in file_system:
        raise HTTPException(status_code=404, detail="File not found")
    return {"path": path, "content": file_system[path]}

@router.post("/delete")
async def delete_file(path: str):
    if path not in file_system:
        raise HTTPException(status_code=404, detail="File not found")
    del file_system[path]
    return {"status": "deleted"}
