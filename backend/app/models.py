from sqlalchemy import Column, Integer, String
from .database import Base


class Player(Base):

    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    skill_rating = Column(Integer, default=5)

    goals = Column(Integer, default=0)

    assists = Column(Integer, default=0)

    mvp_count = Column(Integer, default=0)

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

    status = Column(String, default="Scheduled")