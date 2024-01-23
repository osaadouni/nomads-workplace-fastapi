from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Float, desc
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Place(BaseModel):
    name: str
    description: str | None = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    # class Config:
    #     from_attributes = True

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Cozy Brews",
                    "description": "A charming cafe in the heart of New York City",
                    "coffee": True,
                    "wifi": True,
                    "food": True,
                    "lat": 40.7128,  # Latitude for New York City
                    "lng": -74.0060  # Longitude for New York City
                }
            ]
        }
    }


class DBPlace(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)
    coffee = Column(Boolean, default=False)
    wifi = Column(Boolean, default=False)
    food = Column(Boolean, default=False)
    lat = Column(Float)
    lng = Column(Float)



# db functions
def get_place(db: Session, place_id: int):
    return db.query(DBPlace).where(DBPlace.id == place_id).first()


def get_places(db: Session):
    # return db.query(DBPlace).all()
    return db.query(DBPlace).order_by(desc(DBPlace.id)).all()


def create_place(db: Session, place: Place):
    db_place = DBPlace(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

    return db_place


def delete_place(db: Session, place_id: int):
    # return db.delete(DBPlace).where(DBPlace.id == place_id)
    place = db.query(DBPlace).filter(DBPlace.id == place_id).first()
    if place:
        db.delete(place)
        db.commit()
        return True
    return False


def update_place(db: Session, place_id: int, place: Place) -> bool:
    print("update_place()")
    db_place = db.query(DBPlace).filter(DBPlace.id == place_id).one_or_none()
    if db_place is None:
        return None
    # Update model class variable from request fields
    for var, value in vars(place).items():
        setattr(db_place, var, value) if value else None
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place