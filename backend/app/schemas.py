from pydantic import BaseModel


class PlayerCreate(BaseModel):
    name: str
    skill_rating: int = 5


class PlayerResponse(BaseModel):
    id: int
    name: str
    skill_rating: int

    class Config:
        from_attributes = True

from datetime import date


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