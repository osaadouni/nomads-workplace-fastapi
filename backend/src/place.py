from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import (
    Place,
    create_place,
    get_places,
    get_place,
    delete_place,
    update_place
)

router = APIRouter()

@router.post("/places/", response_model=Place)
async def create_place_view(place: Place, db: Session = Depends(get_db)):
    db_place = create_place(db, place)
    return db_place

# @router.get("/places/", response_model=list[Place])
@router.get("/places/")
def get_places_view(db: Session = Depends(get_db)):
    return get_places(db)

@router.get("/place/{place_id}")
def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return get_place(db, place_id)

@router.put("/places/{place_id}")
def update_place_view(place_id: int, place: Place, db: Session = Depends(get_db)):
    print("update_place func called!")
    print(f"place_id: {place_id}; place: {place}")
    result = update_place(db, place_id, place)
    if result is None:
        return {"message": "Failed to update place", "status": "failed"}

    return {"status": "success",
            "message": "Place updated successfully",
            "db_place": result}


@router.delete("/place/{place_id}")
def delete_place_view(place_id: int, db: Session = Depends(get_db)):
    deleted = delete_place(db, place_id)
    if deleted:
        return {"success": "Place deleted successfully"}
    else:
        return {"error": "Place not found"}

# requests and views
@router.get('/')
async def root():
    return {'message': 'Hello World!'}
