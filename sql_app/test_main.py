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
    response = client.post("/users", json={"username":"坂井"})

    assert response.status_code == 200
    assert response.json() != None

def test_create_rooms():
    response = client.post("/rooms", json={"room_name":"大会議室","capacity":12})

    assert response.status_code == 200
    assert response.json() != None

def test_create_bookings():
    response = client.post(
        "/bookings",
        json={
            "room_id": 3,
            "user_id": 1,
            "booked_num": 6,
            "start_datetime": "2021-12-29T07:15:33.592Z",
            "end_datetime": "2021-12-29T07:45:33.592Z"
        },
    )
    assert response.status_code == 200
    assert response.json() != {"detail": "Already booked!"}

    response = client.post(
        "/bookings",
        json={
            "room_id": 3,
            "user_id": 2,
            "booked_num": 10,
            "start_datetime": "2021-12-29T07:00:33.592Z",
            "end_datetime": "2021-12-29T07:30:33.592Z"
        },
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Already booked!"}

