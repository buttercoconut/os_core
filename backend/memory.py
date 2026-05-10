"""Memory management module with simple allocation/deallocation."""

from fastapi import APIRouter
from typing import Dict

router = APIRouter()

# Simple memory map: address -> size
memory_map: Dict[int, int] = {}
next_address = 0x1000

@router.post("/allocate")
async def allocate(size: int):
    global next_address
    addr = next_address
    memory_map[addr] = size
    next_address += size
    return {"address": addr, "size": size}

@router.post("/free")
async def free(address: int):
    if address not in memory_map:
        return {"error": "Invalid address"}
    del memory_map[address]
    return {"status": "freed"}
