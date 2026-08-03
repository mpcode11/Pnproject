from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models, schemas


router = APIRouter(
    prefix="/players",
    tags=["Players"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_player(
    player: schemas.PlayerCreate,
    db: Session = Depends(get_db)
):

    new_player = models.Player(
        name=player.name,
        skill_rating=player.skill_rating
    )

    db.add(new_player)
    db.commit()
    db.refresh(new_player)

    return new_player

@router.get("/")
def get_players(db: Session = Depends(get_db)):

    players = db.query(models.Player).all()

    return players


@router.get("/search")  
def search_players(
    name: str,
    db: Session = Depends(get_db)
):

    players = db.query(models.Player).filter(
        models.Player.name.contains(name)
    ).all()

    return players