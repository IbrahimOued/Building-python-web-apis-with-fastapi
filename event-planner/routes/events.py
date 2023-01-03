from fastapi import APIRouter, Body, HTTPException, status
from database.connection import Database
from beanie import PydanticObjectId
from models.events import Event, EventUpdate
from typing import List
event_database = Database(Event)

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    await event_database.save(body)
    events.append(body)
    return {
        "message": "Event created successfully"
    }

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return { "message": "Event deleted successfully" }

    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message": "Event deleted successfully."
    }
    
@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event
