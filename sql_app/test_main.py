from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() != None

def test_read_rooms():
    response = client.get("/rooms")
    assert response.status_code == 200
    assert response.json() != None

def test_read_bookings():
    response = client.get("/bookings")
    assert response.status_code == 200
    assert response.json() != None

def test_create_users():
    response = client.post("/users", json={"username":"福永"})

    assert response.status_code == 200
    assert response.json() != None

def test_create_rooms():
    response = client.post("/rooms", json={"room_name":"1on1面談室","capacity":2})

    assert response.status_code == 200
    assert response.json() != None

def test_create_bookings():
    response = client.post(
        "/bookings",
        json={
            "room_id": 1,
            "user_id": 1,
            "booked_num": 5,
            "start_datetime": "2021-12-25T08:00:41.375Z",
            "end_datetime": "2021-12-25T08:30:39.394Z"
        },
    )
    assert response.status_code == 200
    assert response.json() != {"detail": "Already booked!"}

    response = client.post(
        "/bookings",
        json={
            "room_id": 1,
            "user_id": 2,
            "booked_num": 3,
            "start_datetime": "2021-12-25T08:15:41.375Z",
            "end_datetime": "2021-12-25T08:45:39.394Z"
        },
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Already booked!"}

