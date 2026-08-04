from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base



event_players = Table(
    "event_players",
    Base.metadata,
    Column(
        "event_id",
        Integer,
        ForeignKey("events.id")
    ),
    Column(
        "player_id",
        Integer,
        ForeignKey("players.id")
    )
)
class Player(Base):

    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    skill_rating = Column(Integer, default=5)

    goals = Column(Integer, default=0)

    assists = Column(Integer, default=0)

    mvp_count = Column(Integer, default=0)
    events = relationship(
    "Event",
    secondary=event_players,
    back_populates="players"
)
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date
from datetime import date


class Match(Base):

    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    host_name = Column(String, nullable=False)

    match_type = Column(String, nullable=False)

    match_date = Column(Date, default=date.today)

    status = Column(String, default="Scheduled")
   

class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    host_name = Column(String, nullable=False)

    event_type = Column(String, nullable=False)

    match_type = Column(String, nullable=False)

    event_date = Column(Date, default=date.today)

    status = Column(String, default="Scheduled")
players = relationship(
    "Player",
    secondary=event_players,
    back_populates="events"
)

