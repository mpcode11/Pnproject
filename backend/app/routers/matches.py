from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(
    prefix="/matches",
    tags=["Matches"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_match(
    match: schemas.MatchCreate,
    db: Session = Depends(get_db)
):

    new_match = models.Match(
        host_name=match.host_name,
        match_type=match.match_type
    )

    db.add(new_match)
    db.commit()
    db.refresh(new_match)

    return new_match