"""Process management module with simple Round Robin scheduler."""

from fastapi import APIRouter, HTTPException
from typing import List
from .include.os_types import Process

router = APIRouter()

# In-memory process table
process_table: List[Process] = []

# Simple Round Robin scheduler state
rr_index = 0

@router.get("/list")
async def list_processes():
    return process_table

@router.post("/create")
async def create_process(name: str):
    pid = len(process_table) + 1
    proc = Process(pid=pid, name=name, state="ready")
    process_table.append(proc)
    return proc

@router.post("/schedule")
async def schedule_next():
    global rr_index
    if not process_table:
        raise HTTPException(status_code=404, detail="No processes to schedule")
    rr_index = (rr_index + 1) % len(process_table)
    proc = process_table[rr_index]
    proc.state = "running"
    return proc
