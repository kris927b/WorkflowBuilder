import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.session import Base
from app.api.v1.dependencies import get_db

# Database URL for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory SQLite database

# Set up the database engine and session for testing
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency with a test database session
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# Create the database tables for testing
Base.metadata.create_all(bind=engine)

# Create a TestClient instance to interact with the FastAPI app
client = TestClient(app)


@pytest.fixture(scope="module")
def test_client():
    # Provides a test client instance for the tests
    with TestClient(app) as c:
        yield c


# Define the test user data for registration and login
test_user = {"email": "testuser@example.com", "password": "testpassword"}


def test_register_user(test_client):
    # Test the user registration endpoint
    response = test_client.post("/auth/register", json=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_user(test_client):
    # Test the user login endpoint
    response = test_client.post("/auth/login", json=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_register_existing_user(test_client):
    # Test registration with an existing user
    response = test_client.post("/auth/register", json=test_user)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_login_invalid_user(test_client):
    # Test login with incorrect credentials
    response = test_client.post(
        "/auth/login",
        json={"email": "invalid@example.com", "password": "wrongpassword"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid email or password"


def test_login_wrong_password(test_client):
    # Test login with the correct email but wrong password
    response = test_client.post(
        "/auth/login", json={"email": test_user["email"], "password": "wrongpassword"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid email or password"
