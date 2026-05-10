"""Interrupt handling module (placeholder)."""

from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def interrupt_status():
    return {"interrupts": []}
