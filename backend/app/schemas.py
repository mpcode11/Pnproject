from pydantic import BaseModel
from datetime import date

#player schema 
class PlayerCreate(BaseModel):
    name: str
    skill_rating: int = 5


class PlayerResponse(BaseModel):
    id: int
    name: str
    skill_rating: int

    class Config:
        from_attributes = True

#matches schema 


class MatchCreate(BaseModel):

    host_name: str

    match_type: str


class MatchResponse(BaseModel):

    id: int

    host_name: str

    match_type: str

    match_date: date

    status: str

    class Config:
        from_attributes = True

    #events schema

class EventCreate(BaseModel):
    host_name: str
    event_type: str
    match_type: str


class EventResponse(BaseModel):
    id: int
    host_name: str
    event_type: str
    match_type: str
    event_date: date
    status: str

    class Config:
        from_attributes = True