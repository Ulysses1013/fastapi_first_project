import datetime
from pydantic import BaseModel, Field

#予約クラス
class BookingCreate(BaseModel):
    room_id: int
    user_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

class Booking(BookingCreate):
    booking_id: int

    class Config:
        orm_mode = True

#ユーザークラス
class UserCreate(BaseModel):
    username: str = Field(max_length=12)

class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

#会議室クラス
class RoomCreate(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int


class Room(RoomCreate):
    room_id: int

    class Config:
        orm_mode = True