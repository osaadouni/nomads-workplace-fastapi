
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.main import app, get_db
from src.database import Base
from src.models import Place


# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the in-memory database
Base.metadata.create_all(bind=engine)

# Override the database dependency to use the in-memory database
app.dependency_overrides[get_db] = lambda: TestingSessionLocal()

# Initialize the test client
client = TestClient(app)

def test_create_place():
    place_data = {"name": "Test Place", "description": "Test Description"}
    response = client.post("/places/", json=place_data)
    assert response.status_code == 200
    assert response.json() == {"name": "Test Place", "description": "Test Description", "id": 1}

def test_get_places():
    response = client.get("/places/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_place():
    response = client.get("/place/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json().get("id") == 1

def test_update_place():
    place_data = {"name": "Updated Place", "description": "Updated Description"}
    response = client.put("/places/1", json=place_data)
    assert response.status_code == 200
    assert response.json().get("status") == "success"

def test_delete_place():
    response = client.delete("/place/1")
    assert response.status_code == 200
    assert response.json().get("success") == "Place deleted successfully"

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
