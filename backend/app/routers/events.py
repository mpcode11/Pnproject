from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Event
@router.post("/", response_model=schemas.EventResponse)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    new_event = models.Event(
        host_name=event.host_name,
        event_type=event.event_type,
        match_type=event.match_type
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


# Get All Events
@router.get("/", response_model=list[schemas.EventResponse])
def get_events(db: Session = Depends(get_db)):
    return db.query(models.Event).all()